from representacion_vectorizada_documentos import *
from flujos_experimentales import *
from time import time


input = 'input files/corpus.txt'

print("creando listado de palabras con frecuencia 1")
words_frequency_1 = crear_listado_palabras_frecuencia_1(input)
print("Ya se creó el listado")

print("-- Comenzó preprocesamiento --")
start_time = time()
one_hot_paralelize(input, False, flujo_experimental_2, words_frequency_1)
elapsed_time = time() - start_time
print("-- Finalizó preprocesamiento --")
print("Tiempo utilizado: %.10f segundos." % elapsed_time)
