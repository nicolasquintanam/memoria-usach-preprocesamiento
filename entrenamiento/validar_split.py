file1 = open('flujo_base/out_flujo_base_1_tenders_id_validation.txt', 'r')
file2 = open('flujo_base/out_flujo_base_2_tenders_id_validation.txt', 'r')
file3 = open('flujo_base/out_flujo_base_3_tenders_id_validation.txt', 'r')
file4 = open('flujo_base/out_flujo_base_4_tenders_id_validation.txt', 'r')
file5 = open('flujo_base/out_flujo_base_5_tenders_id_validation.txt', 'r')

lineas1 = file1.readlines()
lineas2 = file2.readlines()
lineas3 = file3.readlines()
lineas4 = file4.readlines()
lineas5 = file5.readlines()

ids = []
for linea in lineas1:
  id = linea.replace('\n', '')
  if(id in ids):
    print('algo mal')
  else:
    ids.append(id)

for linea in lineas2:
  id = linea.replace('\n', '')
  if(id in ids):
    print('algo mal')
  else:
    ids.append(id)

for linea in lineas3:
  id = linea.replace('\n', '')
  if(id in ids):
    print('algo mal')
  else:
    ids.append(id)

for linea in lineas4:
  id = linea.replace('\n', '')
  if(id in ids):
    print('algo mal')
  else:
    ids.append(id)

for linea in lineas5:
  id = linea.replace('\n', '')
  if(id in ids):
    print('algo mal')
  else:
    ids.append(id)
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
print('Todo bien')

for i in range(5):
  file1 = open('flujo_base/out_flujo_base_'+str(i+1)+'_tenders_id_validation.txt')
  file2 = open('flujo_base/out_flujo_base_'+str(i+1)+'_tenders_id_train.txt')

  lines1 = file1.readlines()
  lines2 = file2.readlines()

  validar = []
  for elemento in lines1:
    elemento = elemento.replace('\n', '')
    if(elemento not in validar):
      validar.append(elemento)
    else:
      print('algo mal')

  for elemento in lines2:
    elemento = elemento.replace('\n', '')
    if(elemento not in validar):
      validar.append(elemento)
    else:
      print('algo mal')

  print(len(validar))
  print('Todo bien')

  file1.close()
  file2.close()


file0 = open('validacion/flujo_base_tenders-id.txt')
file1 = open('validacion/flujo_experimental_1_tenders-id.txt')
file2 = open('validacion/flujo_experimental_2_tenders-id.txt')
file3 = open('validacion/flujo_experimental_3_tenders-id.txt')
file4 = open('validacion/flujo_experimental_4_tenders-id.txt')
file5 = open('validacion/flujo_experimental_5_tenders-id.txt')
file6 = open('validacion/flujo_experimental_6_tenders-id.txt')
file7 = open('validacion/flujo_experimental_7_tenders-id.txt')
file8 = open('validacion/flujo_experimental_8_tenders-id.txt')
file9 = open('validacion/flujo_experimental_9_tenders-id.txt')
file10 = open('validacion/flujo_experimental_10_tenders-id.txt')

lineas0 = file0.readlines()
lineas1 = file1.readlines()
lineas2 = file2.readlines()
lineas3 = file3.readlines()
lineas4 = file4.readlines()
lineas5 = file5.readlines()
lineas6 = file6.readlines()
lineas7 = file7.readlines()
lineas8 = file8.readlines()
lineas9 = file9.readlines()
lineas10 = file10.readlines()

validacion = []
for i in range(len(lineas1)):
  if(lineas0[i] == lineas1[i] and lineas0[i] == lineas2[i] and lineas0[i] == lineas3[i] and lineas0[i] == lineas4[i] and lineas0[i] == lineas5[i] and lineas0[i] == lineas6[i] and lineas0[i] == lineas7[i] and lineas0[i] == lineas8[i] and lineas0[i] == lineas8[i] and lineas0[i] == lineas10[i]):
    validacion.append(lineas1[i])
  else:
    print('hay algo mal')
if(len(validacion) == len(lineas1)):
  print('todo bien')
file0.close()
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()
file10.close()