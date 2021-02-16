from representacion_vectorizada_documentos import *
from flujos_experimentales import *
from time import time
import csv


input = 'input files/corpus100.txt'

print("creando listado de palabras con frecuencia 1")
words_frequency_1 = crear_listado_palabras_frecuencia_1(input)
print("Ya se creó el listado")

print("-- Comenzó preprocesamiento con flujo_base --")
one_hot_paralelize(input, False, flujo_base, words_frequency_1, 'flujo_base')
print("-- Finalizó preprocesamiento --")

print("-- Comenzó preprocesamiento con flujo_experimental 1 --")
one_hot_paralelize(input, True, flujo_experimental_1, words_frequency_1, 'flujo_experimental_1')
print("-- Finalizó preprocesamiento --")

print("-- Comenzó preprocesamiento con flujo_experimental 2 --")
one_hot_paralelize(input, False, flujo_experimental_2, words_frequency_1, 'flujo_experimental_2')
print("-- Finalizó preprocesamiento --")

print("-- Comenzó preprocesamiento con flujo_experimental 3 --")
one_hot_paralelize(input, True, flujo_experimental_3, words_frequency_1, 'flujo_experimental_3')
print("-- Finalizó preprocesamiento --")

print("-- Comenzó preprocesamiento con flujo_experimental 4 --")
one_hot_paralelize(input, True, flujo_experimental_4, words_frequency_1, 'flujo_experimental_4')
print("-- Finalizó preprocesamiento --")

print("-- Comenzó preprocesamiento con flujo_experimental 5 --")
one_hot_paralelize(input, False, flujo_experimental_5, words_frequency_1, 'flujo_experimental_5')
print("-- Finalizó preprocesamiento --")

print("-- Comenzó preprocesamiento con flujo_experimental 6 --")
one_hot_paralelize(input, True, flujo_experimental_6, words_frequency_1, 'flujo_experimental_6')
print("-- Finalizó preprocesamiento --")

print("-- Comenzó preprocesamiento con flujo_experimental 7 --")
one_hot_paralelize(input, False, flujo_experimental_7, words_frequency_1, 'flujo_experimental_7')
print("-- Finalizó preprocesamiento --")

print("-- Comenzó preprocesamiento con flujo_experimental 8 --")
one_hot_paralelize(input, False, flujo_experimental_8, words_frequency_1, 'flujo_experimental_8')
print("-- Finalizó preprocesamiento --")

print("-- Comenzó preprocesamiento con flujo_experimental 9 --")
one_hot_paralelize(input, False, flujo_experimental_9, words_frequency_1, 'flujo_experimental_9')
print("-- Finalizó preprocesamiento --")

print("-- Comenzó preprocesamiento con flujo_experimental 10 --")
one_hot_paralelize(input, True, flujo_experimental_10, words_frequency_1, 'flujo_experimental_10')
print("-- Finalizó preprocesamiento --")