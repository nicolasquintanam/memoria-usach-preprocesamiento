from representacion_vectorizada_documentos import *
from flujos_experimentales import *
from time import time


input = 'input files/corpus.txt'

print("creando listado de palabras con frecuencia 1")
words_frequency_1 = crear_listado_palabras_frecuencia_1(input)
print("Ya se creó el listado")

print("-- Comenzó preprocesamiento --")
one_hot_paralelize(input, False, flujo_base, words_frequency_1, 'flujo_base')
print("-- Finalizó preprocesamiento --")

"""
Naive Bayes
"""
########## LIBRERÍAS A UTILIZAR ##########
#Se importan la librerias a utilizar
#from sklearn import datasets
########## PREPARAR LA DATA ##########
#Importamos los datos de la misma librería de scikit-learn
#iris = datasets.load_iris()
#print(len(iris.target))
#print(len(iris.data))