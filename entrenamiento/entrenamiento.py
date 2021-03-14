from time import time
import csv
import multiprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import getopt
import sys

flujo = ''

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
        flujo = arg

filename_abstract_test_group = 'abstract/test_' + flujo + '.txt'
filename_abstract = 'abstract/' + flujo + '.txt'
file_abstract_test_group = open(filename_abstract_test_group, 'w')
file_abstract = open(filename_abstract, 'w')
list_accuracy_test_group = []
list_accuracy = []
for j in range(2):
    # --- INICIO ENTRENAMIENTO
    filename_train_dataset = flujo + '/out_' + flujo + '_' + str(j+1) + '_dataset_train.csv'
    filename_train_categories = flujo + '/out_' + flujo + '_' + str(j+1) + '_categories_train.txt'

    algoritmo = MultinomialNB()

    file_train_dataset = open(filename_train_dataset, 'r')
    file_train_categories = open(filename_train_categories, 'r')
    lineass = file_train_categories.readlines()
    i = 0

    for element in file_train_dataset:
        element = element.replace('\n', '').split(';')
        map_object = map(int, element)
        X = list(map_object)
        a = int(lineass[i])
        asdf = []
        asdf.append(a)
        array = []
        array.append(X)
        i = i + 1
        print(i)
        algoritmo.partial_fit(np.array(array), np.array(asdf), classes=np.unique([1,2,3,4,5]))
    #---- FIN ENTRENAMIENTO

    #---- INICIO PREDICCIÓN GRUPO DE VALIDACIÓN
    filename_validation_dataset = flujo + '/out_' + flujo + '_'+str(j+1)+'_dataset_validation.csv'
    filename_validation_categories = flujo + '/out_' + flujo + '_'+str(j+1)+'_categories_validation.txt'
    file_validation_dataset = open(filename_validation_dataset, 'r')
    file_validation_categories = open(filename_validation_categories, 'r')
    lineas_dataset_validation = file_validation_dataset.readlines()
    lineas_categories_validation = file_validation_categories.readlines()

    y_validation = []
    categories_rial = []
    i = 0
    for elemento in lineas_dataset_validation:
        elemento = elemento.replace('\n', '').split(';')
        map_object = map(int, elemento)
        X = list(map_object)
        categories_rial.append(int(lineas_categories_validation[i]))
        i = i + 1
        y_validation.append(X)

    y_pred = algoritmo.predict(np.array(y_validation))
    matriz = confusion_matrix(categories_rial, y_pred)
    exactitud = accuracy_score(categories_rial, y_pred)
    list_accuracy.append(exactitud)
    exactitud = accuracy_score(categories_rial, y_pred)
    matriz = confusion_matrix(categories_rial, y_pred)
    file_abstract.write('Iteration ' + str(j+1) + ': \n\n')
    file_abstract.write('Accuracy = ' + str(exactitud) + '\n\n')
    file_abstract.write('Confusion Matrix \n\n')
    file_abstract.write(np.array2string(matriz, separator=', '))
    file_abstract.write('\n\n')
    file_abstract.write('-----------------------------------')
    file_abstract.write('\n\n')
    #----- FIN PREDICCIÓN GRUPO DE VALIDACIÓN
    #----- INICIO PREDICCIÓN GRUPO DE TEST
    filename_test_dataset = flujo + '/out_' + flujo + '_dataset_test.csv'
    filename_test_categories = flujo + '/out_' + flujo + '_tenders-category-test.txt'
    file_test_dataset = open(filename_test_dataset, 'r')
    file_test_categories = open(filename_test_categories, 'r')
    lineas_dataset_test = file_test_dataset.readlines()
    lineas_categories_test = file_test_categories.readlines()

    y_test = []
    categories_rial = []
    i = 0
    for elemento in lineas_dataset_test:
        elemento = elemento.replace('\n', '').split(';')
        map_object = map(int, elemento)
        X = list(map_object)
        categories_rial.append(int(lineas_categories_test[i]))
        i = i + 1
        y_test.append(X)

    y_pred = algoritmo.predict(np.array(y_test))
    matriz = confusion_matrix(categories_rial, y_pred)
    exactitud = accuracy_score(categories_rial, y_pred)
    list_accuracy_test_group.append(exactitud)
    exactitud = accuracy_score(categories_rial, y_pred)
    matriz = confusion_matrix(categories_rial, y_pred)
    file_abstract_test_group.write('Iteration ' + str(j+1) + ': \n\n')
    file_abstract_test_group.write('Accuracy = ' + str(exactitud) + '\n\n')
    file_abstract_test_group.write('Confusion Matrix \n\n')
    file_abstract_test_group.write(np.array2string(matriz, separator=', '))
    file_abstract_test_group.write('\n\n')
    file_abstract_test_group.write('-----------------------------------')
    file_abstract_test_group.write('\n\n')
    #----- FIN PREDICCIÓN GRUPO DE TEST

    file_validation_dataset.close()
    file_validation_categories.close()
    file_train_dataset.close()
    file_train_categories.close()
    file_test_dataset.close()
    file_test_categories.close()
    print('finalizó iteración ' + str(j+1) + ' del ' + flujo)

accuracy_average = sum(list_accuracy)/len(list_accuracy)
accuracy_average_test_group = sum(list_accuracy_test_group)/len(list_accuracy_test_group)
file_abstract.write('ACCURACY AVERAGE = ' + str(accuracy_average))
file_abstract_test_group.write('ACCURACY AVERAGE = ' + str(accuracy_average_test_group))
file_abstract.close()
file_abstract_test_group.close()