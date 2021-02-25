#Este script es para dividir Entrenamiento, Validación y Test de cada dataset.

nrows = 32529
experimentation_name = 'flujo_base'
percent_train = 70
percent_test = 30

filename_dataset_complete = experimentation_name + '_dataset.csv'
filename_categories_dataset = experimentation_name + '_tenders-category.txt'
filename_tenders_id = experimentation_name + '_tenders-id.txt'

tenders_id_train_group = []
tenders_id_test_group = []

filename_dataset_train = experimentation_name + '_dataset_train.csv'
filename_categories_train = experimentation_name + '_tenders-category-train.txt'
filename_dataset_test = experimentation_name + '_dataset_test.csv'
filename_categories_test = experimentation_name + '_tenders-category-test.txt'




count_class_1 = 0
count_class_2 = 0
count_class_3 = 0
count_class_4 = 0
count_class_5 = 0
c1tr = 0
c2tr = 0
c3tr = 0
c4tr = 0 
c5tr = 0
c1te = 0
c2te = 0
c3te = 0
c4te = 0 
c5te = 0

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
file_categories = open(filename_categories_dataset, 'r')

print('-----------------------------')
print('----- DATASET COMPLETO ------')
print('---- (100% - '+str(nrows)+' docs) ----')
print('-----------------------------')
print(str(count_class_1/32529*100)+ ' % - Clase 1 - ' + str(count_class_1) + ' docs')
print(str(count_class_2/32529*100)+ ' % - Clase 2 - ' + str(count_class_2) + ' docs')
print(str(count_class_3/32529*100)+ ' % - Clase 3 - ' + str(count_class_3) + ' docs')
print(str(count_class_4/32529*100)+ ' % - Clase 4 - ' + str(count_class_4) + ' docs')
print(str(count_class_5/32529*100)+ ' % - Clase 5 - ' + str(count_class_5) + ' docs')

file_tenders_id = open(filename_tenders_id, 'r')
ids = file_tenders_id.readlines()
print('asdfds')
print(len(ids))
print(len(list(set(ids))))
categories = file_categories.readlines()
for i in range(nrows):
  id = ids[i].replace('\n', '')  
  category = categories[i].replace('\n', '')
  if(category == '1'):
    if(c1tr < count_class_1 * percent_train / 100):
      tenders_id_train_group.append(id)
      c1tr += 1
    else:
      tenders_id_test_group.append(id)
      c1te += 1
  if(category == '2'):
    if(c2tr < count_class_2 * percent_train / 100):
      tenders_id_train_group.append(id)
      c2tr += 1
    else:
      tenders_id_test_group.append(id)
      c2te += 1        
  if(category == '3'):
    if(c3tr < count_class_3 * percent_train / 100):
      tenders_id_train_group.append(id)
      c3tr += 1
    else:
      tenders_id_test_group.append(id)
      c3te += 1        
  if(category == '4'):
    if(c4tr < count_class_4 * percent_train / 100):
      tenders_id_train_group.append(id)
      c4tr += 1
    else:
      tenders_id_test_group.append(id)
      c4te += 1
  if(category == '5'):
    if(c5tr < count_class_5 * percent_train / 100):
      tenders_id_train_group.append(id)
      c5tr += 1
    else:
      c5te += 1
      tenders_id_test_group.append(id)

print('-----------------------------')
print('--- DATASET ENTRENAMIENTO ---')
print('---- ('+ str(percent_train) +'% - '+str(len(tenders_id_train_group))+' docs) -----')
print('-----------------------------')
print(str(c1tr/(32529*percent_train/100)*100) + ' % - Clase 1 - ' + str(c1tr) + ' docs')
print(str(c2tr/(32529*percent_train/100)*100) + ' % - Clase 2 - ' + str(c2tr) + ' docs')
print(str(c3tr/(32529*percent_train/100)*100) + ' % - Clase 3 - ' + str(c3tr) + ' docs')
print(str(c4tr/(32529*percent_train/100)*100) + ' % - Clase 4 - ' + str(c4tr) + ' docs')
print(str(c5tr/(32529*percent_train/100)*100) + ' % - Clase 5 - ' + str(c5tr) + ' docs')
print('-----------------------------')
print('----- DATASET PRUEBAS -------')
print('---- ('+ str(percent_test) +'% - '+str(len(tenders_id_test_group))+' docs) ------')
print('-----------------------------')
print(str(c1te/(32529*percent_test/100)*100) + ' % - Clase 1 - ' + str(c1te) + ' docs')
print(str(c2te/(32529*percent_test/100)*100) + ' % - Clase 2 - ' + str(c2te) + ' docs')
print(str(c3te/(32529*percent_test/100)*100) + ' % - Clase 3 - ' + str(c3te) + ' docs')
print(str(c4te/(32529*percent_test/100)*100) + ' % - Clase 4 - ' + str(c4te) + ' docs')
print(str(c5te/(32529*percent_test/100)*100) + ' % - Clase 5 - ' + str(c5te) + ' docs')
file_tenders_id.close()
file_categories.close()

file_categories = open(filename_categories_dataset, 'r')
file_dataset_complete = open(filename_dataset_complete, 'r')
file_tenders_id = open(filename_tenders_id, 'r')
file_dataset_train = open(filename_dataset_train, 'w')
file_categories_train = open(filename_categories_train, 'w')
file_dataset_test = open(filename_dataset_test, 'w')
file_categories_test = open(filename_categories_test, 'w')

lines_categories_complete = file_categories.readlines()
lines_dataset_complete = file_dataset_complete.readlines()
lines_tenders_id = file_tenders_id.readlines()
print(len(tenders_id_train_group))
print(len(tenders_id_test_group))

i_entr = 0
i_test = 0
for i in range(nrows):
  data = lines_dataset_complete[i]
  data = data.replace('\n', '')
  tender_id = lines_tenders_id[i].replace('\n', '')
  k = 0
  if(tender_id in tenders_id_train_group):
    i_entr = i_entr + 1
    file_dataset_train.write(data)
    file_categories_train.write(lines_categories_complete[i])
    file_dataset_train.write('\n')
  else:
    if(tender_id in tenders_id_test_group):
      i_test = i_test + 1
      file_dataset_test.write(data)
      file_categories_test.write(lines_categories_complete[i])
      file_dataset_test.write('\n')

print(i_entr)
print(i_test)