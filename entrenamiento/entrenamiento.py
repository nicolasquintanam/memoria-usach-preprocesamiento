from time import time
import csv
import multiprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
import getopt
import sys

flujo = 'flujo_base'

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


filename_train_dataset = flujo + '/out_' + flujo + '_2_dataset_train.csv'
filename_train_categories = flujo + '/out_' + flujo + '_2_categories_train.txt'

algoritmo = MultinomialNB()

file_train_dataset = open(filename_train_dataset, 'r')
file_train_categories = open(filename_train_categories, 'r')
lineass = file_train_categories.readlines()
i = 0

xx = []
yy = []
for element in file_train_dataset:
    element = element.replace('\n', '').split(';')
    map_object = map(int, element)
    X = list(map_object)
    a = int(lineass[i])
    asdf = []
    asdf.append(a)
    array = []
    array.append(X)
    #xx.append(np.array(X))
    #yy.append(a)
    #print(np.array(asdf))
    #print(np.array(array))
    #print(np.unique([1,2,3,4,5]))
    print(i)
    algoritmo.partial_fit(np.array(array), np.array(asdf), classes=np.unique([1,2,3,4,5]))
    i = i + 1

#algoritmo.fit(xx, yy)

filename_test_dataset = flujo + '/out_' + flujo + '_2_dataset_validation.csv'
filename_test_categories = flujo + '/out_' + flujo + '_2_categories_validation.txt'
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


print('la cantidad de líneas en y_test es = ' + str(len(y_test)))
y_pred = algoritmo.predict(np.array(y_test))
print(y_pred)
print(categories_rial)
matriz = confusion_matrix(categories_rial, y_pred)
print(matriz)
#print(algoritmo.class_count_)