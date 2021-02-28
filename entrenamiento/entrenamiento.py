from time import time
import csv
import multiprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
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


filename_train_dataset = flujo + '/out_' + flujo + '_1_dataset_train.csv'
filename_train_categories = flujo + '/out_' + flujo + '_1_categories_train.txt'

algoritmo = GaussianNB()

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
    algoritmo.partial_fit(array, asdf, classes=np.unique([1,2,3,4,5]))
    i = i + 1
    print(i)

filename_test_categories = flujo + '/out_' + flujo + '_1_categories_validation.txt'
file_test_categories = open(filename_test_categories, 'r')
lineas_test = file_test_categories.readlines()
y_test = []
for elemento in lineas_test:
    elemento = elemento.replace('\n', '')
    y_test.append(y_test)

print('la cantidad de líneas en y_test es = ' + str(len(y_test)))
y_pred = algoritmo.predict(y_test)
matriz = confusion_matrix(y_test, y_pred)
print(matriz)
print(algoritmo.class_count_)