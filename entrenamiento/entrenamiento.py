from time import time
import csv
import multiprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
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


filename_train_dataset = flujo + '_dataset_train.csv'
filename_train_categories = flujo + '_tenders-category-train.txt'

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
print(algoritmo.class_count_)
'''
file_train_categories = open(filename_train_categories, 'r')
lines = file_train_dataset.readlines()
print(len(lines))
lines_category = file_train_categories.readlines()
for i in range(32529):
    print(i)
    line = lines[i].split(',')
    print(len(line))
    map_object = map(int, line)
    X = list(map_object)
    a = int(lines_category[i].replace('\n', ''))
    asdf = []
    asdf.append(a)
    array = []
    array.append(X)
    algoritmo.partial_fit(array, asdf, classes=np.unique([1,2,3,4,5]))

print(algoritmo.class_count_)
#https://stackoverflow.com/questions/42147302/sklearn-sgd-partial-fit
'''
