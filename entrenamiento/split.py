import getopt
import sys

output_filename = 'flujo_base'

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        'i',
        ['input='])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

for opt, arg in options:
    if opt in ('-i', '--input'):
        output_filename = arg

#Este script es para dividir Entrenamiento, Validación y Test de cada dataset.

experimentation_name = arg
percent_train = 90
percent_test = 10

# --------------- Nombre archivos de dataset completo, categorías y id's de licitaciones --------------
filename_dataset_complete = experimentation_name + '/' + experimentation_name + '_dataset.csv'
filename_categories_dataset = experimentation_name + '/' + experimentation_name + '_tenders-category.txt'
filename_tenders_id = experimentation_name + '/' + experimentation_name + '_tenders-id.txt'

# --------- Nombre archivos de dataset para entrenamiento, categorías y id's de licitaciones ----------
filename_dataset_train = experimentation_name + '/out_' + experimentation_name + '_dataset_train.csv'
filename_categories_train = experimentation_name + '/out_' + experimentation_name + '_tenders-category-train.txt'
filename_tenders_id_train = experimentation_name + '/out_' + experimentation_name + '_tenders-id-train.txt'

# ---------- Nombre archivos de dataset para pruebas, categorías y id's de licitaciones ---------------
filename_dataset_test = experimentation_name + '/out_' + experimentation_name + '_dataset_test.csv'
filename_categories_test = experimentation_name + '/out_' + experimentation_name + '_tenders-category-test.txt'
filename_tenders_id_test = experimentation_name + '/out_' + experimentation_name + '_tenders-id-test.txt'

count_class_1 = 0 # cant. de documentos con clase 1
count_class_2 = 0 # cant. de documentos con clase 2
count_class_3 = 0 # cant. de documentos con clase 3
count_class_4 = 0 # cant. de documentos con clase 4
count_class_5 = 0 # cant. de documentos con clase 5

train_class_1 = 0 # cant. documentos para entrenamiento con la clase 1
train_class_2 = 0 # cant. documentos para entrenamiento con la clase 2
train_class_3 = 0 # cant. documentos para entrenamiento con la clase 3
train_class_4 = 0 # cant. documentos para entrenamiento con la clase 4 
train_class_5 = 0 # cant. documentos para entrenamiento con la clase 5

test_class_1 = 0 # cant. documentos para pruebas con la clase 1
test_class_2 = 0 # cant. documentos para pruebas con la clase 2
test_class_3 = 0 # cant. documentos para pruebas con la clase 3
test_class_4 = 0 # cant. documentos para pruebas con la clase 4
test_class_5 = 0 # cant. documentos para pruebas con la clase 5

tenders_id_train_group = [] # listado de id's de las licitaciones en el grupo de entrenamiento
tenders_id_test_group = []  # listado de id's de las licitaciones en el grupo de pruebas

# ----------------------------------------------------------
# --- Obtención de cantidad de documentos por clase --------
# ----------------------------------------------------------

file_categories = open(filename_categories_dataset, 'r')
for category in file_categories:
  category = category.replace('\n', '')
  if(category == '1'):
    count_class_1 += 1
  if(category == '2'):
    count_class_2 += 1
  if(category == '3'):
    count_class_3 += 1
  if(category == '4'):
    count_class_4 += 1
  if(category == '5'):
    count_class_5 += 1
file_categories.close()

# ----------------------------------------------------
# --------- Resumen del DATASET completo -------------
# ----------------------------------------------------

file_categories = open(filename_categories_dataset, 'r')
categories = file_categories.readlines()
nrows = len(categories)
print('-----------------------------')
print('----- DATASET COMPLETO ------')
print('---- (100% - ' + str(nrows) + ' docs) ----')
print('-----------------------------')
print(str(count_class_1/nrows*100) + ' % - Clase 1 - ' + str(count_class_1) + ' docs')
print(str(count_class_2/nrows*100) + ' % - Clase 2 - ' + str(count_class_2) + ' docs')
print(str(count_class_3/nrows*100) + ' % - Clase 3 - ' + str(count_class_3) + ' docs')
print(str(count_class_4/nrows*100) + ' % - Clase 4 - ' + str(count_class_4) + ' docs')
print(str(count_class_5/nrows*100) + ' % - Clase 5 - ' + str(count_class_5) + ' docs')

# ----------------------------------------------------
# ------ Inicio split para dividir el dataset --------
# --------- entre entrenamiento y pruebas ------------
# ----------------------------------------------------

file_tenders_id = open(filename_tenders_id, 'r')
ids = file_tenders_id.readlines()
for i in range(nrows):
  id = ids[i].replace('\n', '')  
  category = categories[i].replace('\n', '')
  if(category == '1'):
    if(train_class_1 < count_class_1 * percent_train / 100):
      tenders_id_train_group.append(id)
      train_class_1 += 1
    else:
      tenders_id_test_group.append(id)
      test_class_1 += 1
  if(category == '2'):
    if(train_class_2 < count_class_2 * percent_train / 100):
      tenders_id_train_group.append(id)
      train_class_2 += 1
    else:
      tenders_id_test_group.append(id)
      test_class_2 += 1        
  if(category == '3'):
    if(train_class_3 < count_class_3 * percent_train / 100):
      tenders_id_train_group.append(id)
      train_class_3 += 1
    else:
      tenders_id_test_group.append(id)
      test_class_3 += 1        
  if(category == '4'):
    if(train_class_4 < count_class_4 * percent_train / 100):
      tenders_id_train_group.append(id)
      train_class_4 += 1
    else:
      tenders_id_test_group.append(id)
      test_class_4 += 1
  if(category == '5'):
    if(train_class_5 < count_class_5 * percent_train / 100):
      tenders_id_train_group.append(id)
      train_class_5 += 1
    else:
      tenders_id_test_group.append(id)
      test_class_5 += 1

# ------------------------------------------------
# --------- Resumen del split entre  -------------
# --------- entrenamiento y pruebas  -------------
# ------------------------------------------------
print('\n')
print('########################################################')
print('########################################################')
print('\n')
print('-----------------------------')
print('--- DATASET ENTRENAMIENTO ---')
print('---- (' + str(percent_train) + '% - ' + str(len(tenders_id_train_group)) + ' docs) -----')
print('-----------------------------')
print(str(train_class_1/(nrows*percent_train/100)*100) + ' % - Clase 1 - ' + str(train_class_1) + ' docs')
print(str(train_class_2/(nrows*percent_train/100)*100) + ' % - Clase 2 - ' + str(train_class_2) + ' docs')
print(str(train_class_3/(nrows*percent_train/100)*100) + ' % - Clase 3 - ' + str(train_class_3) + ' docs')
print(str(train_class_4/(nrows*percent_train/100)*100) + ' % - Clase 4 - ' + str(train_class_4) + ' docs')
print(str(train_class_5/(nrows*percent_train/100)*100) + ' % - Clase 5 - ' + str(train_class_5) + ' docs')
print('-----------------------------')
print('----- DATASET PRUEBAS -------')
print('---- (' + str(percent_test) + '% - ' + str(len(tenders_id_test_group)) + ' docs) ------')
print('-----------------------------')
print(str(test_class_1/(nrows*percent_test/100)*100) + ' % - Clase 1 - ' + str(test_class_1) + ' docs')
print(str(test_class_2/(nrows*percent_test/100)*100) + ' % - Clase 2 - ' + str(test_class_2) + ' docs')
print(str(test_class_3/(nrows*percent_test/100)*100) + ' % - Clase 3 - ' + str(test_class_3) + ' docs')
print(str(test_class_4/(nrows*percent_test/100)*100) + ' % - Clase 4 - ' + str(test_class_4) + ' docs')
print(str(test_class_5/(nrows*percent_test/100)*100) + ' % - Clase 5 - ' + str(test_class_5) + ' docs')
file_tenders_id.close()
file_categories.close()


file_dataset_complete = open(filename_dataset_complete, 'r')
file_categories = open(filename_categories_dataset, 'r')
file_tenders_id = open(filename_tenders_id, 'r')
lines_dataset_complete = file_dataset_complete.readlines()
lines_categories_complete = file_categories.readlines()
lines_tenders_id = file_tenders_id.readlines()

# ---------------------------------------------------------------------
# --------------- Se crean y escriben los archivos --------------------
# ----- dataset, categorías y id's licitaciones de entrenamiento ------
# ------- y dataset, categorías y id's licitaciones de pruebas --------
# ---------------------------------------------------------------------

file_dataset_train = open(filename_dataset_train, 'w')
file_categories_train = open(filename_categories_train, 'w')
file_tenders_id_train = open(filename_tenders_id_train, 'w')

file_dataset_test = open(filename_dataset_test, 'w')
file_categories_test = open(filename_categories_test, 'w')
file_tenders_id_test = open(filename_tenders_id_test, 'w')


for i in range(nrows):
  data = lines_dataset_complete[i]
  data = data.replace('\n', '')
  tender_id = lines_tenders_id[i].replace('\n', '')
  k = 0
  if(tender_id in tenders_id_train_group):
    file_dataset_train.write(data)
    file_dataset_train.write('\n')
    file_categories_train.write(lines_categories_complete[i])
    file_tenders_id_train.write(tender_id)
    file_tenders_id_train.write('\n')
  else:
    if(tender_id in tenders_id_test_group):
      file_dataset_test.write(data)
      file_categories_test.write(lines_categories_complete[i])
      file_dataset_test.write('\n')
      file_tenders_id_test.write(tender_id)
      file_tenders_id_test.write('\n')

file_categories.close()
file_tenders_id.close()
file_dataset_complete.close()
file_dataset_train.close()
file_categories_train.close()
file_tenders_id_train.close()
file_dataset_test.close()
file_categories_test.close()
file_tenders_id_test.close()

###############################################################
################### SPLIT DE ENTRENAMIENTO ####################
############ PARA VALIDACIÓN CRUZADA CON K-FOLDS ##############
#################### CON 5 ITERACIONES ########################
###############################################################

file_dataset_train = open(filename_dataset_train, 'r')
lines_dataset_train = file_dataset_train.readlines()
count_lines_dataset_train = len(lines_dataset_train)

count_class_1 = 0 # cant. documentos con la clase 1
count_class_2 = 0 # cant. documentos con la clase 2
count_class_3 = 0 # cant. documentos con la clase 3
count_class_4 = 0 # cant. documentos con la clase 4
count_class_5 = 0 # cant. documentos con la clase 5

# ----------------------------------------------------------
# --- Obtención de cantidad de documentos por clase --------
# ----------------------------------------------------------

file_categories_train = open(filename_categories_train, 'r')
for category in file_categories_train:
  category = category.replace('\n', '')
  if(category == '1'):
    count_class_1 += 1
  if(category == '2'):
    count_class_2 += 1
  if(category == '3'):
    count_class_3 += 1
  if(category == '4'):
    count_class_4 += 1
  if(category == '5'):
    count_class_5 += 1
file_categories_train.close()


iterations = 5

file_categories_train = open(filename_categories_train, 'r')
file_tenders_id_train = open(filename_tenders_id_train, 'r')
categories = file_categories_train.readlines()
ids = file_tenders_id_train.readlines()

percent_validation = 100/iterations              # Porcentaje grupo de validación -> 20%
percent_new_train = 100 - percent_validation     # Porcentaje nuevo entrenamiento -> 80%
tenders_id_used_in_validation_group = []         # Listado de id's de licitaciones ya utilizados para el grupo de validación


for i in range(iterations):
  filename_dataset_train_iteration = experimentation_name + '/out_' + experimentation_name + '_' + str(i+1) + '_dataset_train.csv' 
  filename_categories_train_iteration = experimentation_name + '/out_' + experimentation_name + '_' + str(i+1) + '_categories_train.txt'
  filename_tenders_id_train_iteration = experimentation_name + '/out_' + experimentation_name + '_' + str(i+1) + '_tenders_id_train.txt'
  filename_dataset_validation_iteration = experimentation_name + '/out_' + experimentation_name + '_' + str(i+1) + '_dataset_validation.csv'
  filename_categories_validation_iteration = experimentation_name + '/out_' + experimentation_name + '_' + str(i+1) + '_categories_validation.txt'
  filename_tenders_id_validation_iteration = experimentation_name + '/out_' + experimentation_name + '_' + str(i+1) + '_tenders_id_validation.txt'
  file_dataset_train_iteration = open(filename_dataset_train_iteration, 'w')
  file_categories_train_iteration = open(filename_categories_train_iteration, 'w')
  file_tenders_id_train_iteration = open(filename_tenders_id_train_iteration, 'w')
  file_dataset_validation_iteration = open(filename_dataset_validation_iteration, 'w')
  file_categories_validation_iteration = open(filename_categories_validation_iteration, 'w')
  file_tenders_id_validation_iteration = open(filename_tenders_id_validation_iteration, 'w')

  new_train_class_1 = 0   # cant. documentos para entrenamiento con clase 1
  new_train_class_2 = 0   # cant. documentos para entrenamiento con clase 2
  new_train_class_3 = 0   # cant. documentos para entrenamiento con clase 3
  new_train_class_4 = 0   # cant. documentos para entrenamiento con clase 4
  new_train_class_5 = 0   # cant. documentos para entrenamiento con clase 5

  validation_class_1 = 0  # cant. documentos para validación con clase 1
  validation_class_2 = 0  # cant. documentos para validación con clase 2
  validation_class_3 = 0  # cant. documentos para validación con clase 3
  validation_class_4 = 0  # cant. documentos para validación con clase 4
  validation_class_5 = 0  # cant. documentos para validación con clase 5

  tenders_id_train_group_iteration = []       # Listado de id's licitaciones en el grupo de entrenamiento
  tenders_id_validation_group_iteration = []  # Listado de id's licitaciones en el grupo de validación

  # ----------------------------------------------------
  # ------ Inicio split para dividir el dataset --------
  # ------- entre entrenamiento y validación -----------
  # --------------- por iteración ----------------------
  # ----------------------------------------------------

  for j in range(count_lines_dataset_train):
    id = ids[j].replace('\n', '')  
    category = categories[j].replace('\n', '')
    if(category == '1'):
      if(validation_class_1 < count_class_1 * percent_validation / 100):
        if(id not in tenders_id_used_in_validation_group):
          tenders_id_used_in_validation_group.append(id)
          tenders_id_validation_group_iteration.append(id)
          validation_class_1 += 1
        else:
          tenders_id_train_group_iteration.append(id)
          new_train_class_1 += 1
      else:
        tenders_id_train_group_iteration.append(id)
        new_train_class_1 += 1  
    if(category == '2'):
      if(validation_class_2 < count_class_2 * percent_validation / 100):
        if(id not in tenders_id_used_in_validation_group):
          tenders_id_used_in_validation_group.append(id)
          tenders_id_validation_group_iteration.append(id)
          validation_class_2 += 1
        else:
          tenders_id_train_group_iteration.append(id)
          new_train_class_2 += 1
      else:
        tenders_id_train_group_iteration.append(id)
        new_train_class_2 += 1      
    if(category == '3'):
      if(validation_class_3 < count_class_3 * percent_validation / 100):
        if(id not in tenders_id_used_in_validation_group):
          tenders_id_used_in_validation_group.append(id)
          tenders_id_validation_group_iteration.append(id)
          validation_class_3 += 1
        else:
          tenders_id_train_group_iteration.append(id)
          new_train_class_3 += 1
      else:
        tenders_id_train_group_iteration.append(id)
        new_train_class_3 += 1     
    if(category == '4'):
      if(validation_class_4 < count_class_4 * percent_validation / 100):
        if(id not in tenders_id_used_in_validation_group):
          tenders_id_used_in_validation_group.append(id)
          tenders_id_validation_group_iteration.append(id)
          validation_class_4 += 1
        else:
          tenders_id_train_group_iteration.append(id)
          new_train_class_4 += 1
      else:
        tenders_id_train_group_iteration.append(id)
        new_train_class_4 += 1
    if(category == '5'):
      if(validation_class_5 < count_class_5 * percent_validation / 100):
        if(id not in tenders_id_used_in_validation_group):
          tenders_id_validation_group_iteration.append(id)
          tenders_id_used_in_validation_group.append(id)
          validation_class_5 += 1
        else:
          tenders_id_train_group_iteration.append(id)
          new_train_class_5 += 1
      else:
        tenders_id_train_group_iteration.append(id)
        new_train_class_5 += 1
  
  print('\n')
  print('########################################################')
  print('########################################################')
  print('\n')
  print('-----------------------------------------')
  print('--- DATASET ENTRENAMIENTO (ITERACIÓN ' + str(i+1) + ') ---')
  print('---- ('+ str(percent_new_train) + '% - ' + str(len(tenders_id_train_group_iteration)) + ' docs) -----')
  print('-----------------------------------------')
  print(str(new_train_class_1/(count_lines_dataset_train*percent_new_train/100)*100) + ' % - Clase 1 - ' + str(new_train_class_1) + ' docs')
  print(str(new_train_class_2/(count_lines_dataset_train*percent_new_train/100)*100) + ' % - Clase 2 - ' + str(new_train_class_2) + ' docs')
  print(str(new_train_class_3/(count_lines_dataset_train*percent_new_train/100)*100) + ' % - Clase 3 - ' + str(new_train_class_3) + ' docs')
  print(str(new_train_class_4/(count_lines_dataset_train*percent_new_train/100)*100) + ' % - Clase 4 - ' + str(new_train_class_4) + ' docs')
  print(str(new_train_class_5/(count_lines_dataset_train*percent_new_train/100)*100) + ' % - Clase 5 - ' + str(new_train_class_5) + ' docs')
  print('---------------------------------------------')
  print('----- DATASET VALIDACIÓN (ITERACIÓN ' + str(i+1) + ') ---')
  print('---- ('+ str(percent_validation) + '% - '+str(len(tenders_id_validation_group_iteration)) + ' docs) -----')
  print('---------------------------------------------')
  print(str(validation_class_1/(count_lines_dataset_train*percent_validation/100)*100) + ' % - Clase 1 - ' + str(validation_class_1) + ' docs')
  print(str(validation_class_2/(count_lines_dataset_train*percent_validation/100)*100) + ' % - Clase 2 - ' + str(validation_class_2) + ' docs')
  print(str(validation_class_3/(count_lines_dataset_train*percent_validation/100)*100) + ' % - Clase 3 - ' + str(validation_class_3) + ' docs')
  print(str(validation_class_4/(count_lines_dataset_train*percent_validation/100)*100) + ' % - Clase 4 - ' + str(validation_class_4) + ' docs')
  print(str(validation_class_5/(count_lines_dataset_train*percent_validation/100)*100) + ' % - Clase 5 - ' + str(validation_class_5) + ' docs')

  # ---------------------------------------------------------------------
  # -------------------- Se escriben los archivos -----------------------
  # ----- dataset, categorías y id's licitaciones de entrenamiento ------
  # ------ y dataset, categorías y id's licitaciones de validación ------
  # ---------------------------------------------------------------------

  file_categories_train.close()
  file_categories_train = open(filename_categories_train, 'r')
  categories = file_categories_train.readlines()
  file_tenders_id_train.close()
  file_tenders_id_train = open(filename_tenders_id_train, 'r')
  ids = file_tenders_id_train.readlines()
  for j in range(count_lines_dataset_train):
    data = lines_dataset_train[j]
    data = data.replace('\n', '')
    tender_id = ids[j].replace('\n', '')
    k = 0
    if(tender_id in tenders_id_train_group_iteration):
      file_dataset_train_iteration.write(data)
      file_dataset_train_iteration.write('\n')
      file_categories_train_iteration.write(categories[j])
      file_tenders_id_train_iteration.write(tender_id)
      file_tenders_id_train_iteration.write('\n')
    if(tender_id in tenders_id_validation_group_iteration):
      file_dataset_validation_iteration.write(data)
      file_dataset_validation_iteration.write('\n')
      file_categories_validation_iteration.write(categories[j])
      file_tenders_id_validation_iteration.write(tender_id)
      file_tenders_id_validation_iteration.write('\n')
  
  file_dataset_train_iteration.close()
  file_categories_train_iteration.close()
  file_dataset_validation_iteration.close()
  file_categories_validation_iteration.close()
  file_tenders_id_validation_iteration.close()
  file_tenders_id_train_iteration.close()