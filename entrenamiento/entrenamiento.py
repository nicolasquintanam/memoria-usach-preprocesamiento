from time import time
import csv
import multiprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

filename_train_dataset = 'flujo_experimental_3_dataset_train.csv'
filename_train_categories = 'flujo_experimental_3_tenders-category-train.txt'

algoritmo = GaussianNB()

file_train_dataset = open(filename_train_dataset, 'r')
file_train_categories = open(filename_train_categories, 'r')
lines = file_train_dataset.readlines()
lines_category = file_train_categories.readlines()
for i in range(100):
    line = lines[i].replace('\n', '')
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