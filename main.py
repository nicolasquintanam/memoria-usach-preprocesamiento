from representacion_vectorizada_documentos import *
from flujos_experimentales import *
from time import time
import csv

'''
input = 'input files/corpus.txt'

print("creando listado de palabras con frecuencia 1")
words_frequency_1 = crear_listado_palabras_frecuencia_1(input)
print("Ya se creó el listado")

print("-- Comenzó preprocesamiento --")
one_hot_paralelize(input, True, flujo_experimental_1, words_frequency_1, 'flujo_exp_1')
print("-- Finalizó preprocesamiento --")
'''
"""
Naive Bayes
"""
########## LIBRERÍAS A UTILIZAR ##########
#Se importan la librerias a utilizar
from sklearn import datasets
input_dataset = 'input files/flujo_base_dataset.csv'
input_category = 'input files/flujo_base_tenders-category.txt'

dataset = []
f1 = open(input_dataset, 'r')
#f2 = open(input_category, 'r')
lineas_dataset = f1.readlines()
#lineas_category = f2.readlines()

'''for i in range(len(lineas_dataset)):
    linea_dataset = lineas_dataset[i].replace('\n', '')
    linea_category = lineas_category[i].replace('\n', '')
    dataset.append(linea_dataset.split(';'))'''

with open(input_dataset, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

print(len(data))
print(len(data[1]))

########## PREPARAR LA DATA ##########
#Importamos los datos de la misma librería de scikit-learn
