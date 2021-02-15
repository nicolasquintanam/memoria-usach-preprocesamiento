from representacion_vectorizada_documentos import *
from flujos_experimentales import *
from time import time
import csv


input = 'input files/corpus1000.txt'

print("creando listado de palabras con frecuencia 1")
words_frequency_1 = crear_listado_palabras_frecuencia_1(input)
print("Ya se creó el listado")

print("-- Comenzó preprocesamiento con flujo_experimental_3 --")
one_hot_paralelize(input, True, flujo_experimental_3, words_frequency_1, 'flujo_exp_3')
print("-- Finalizó preprocesamiento --")