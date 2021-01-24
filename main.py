from representacion_vectorizada_documentos import *
from flujos_experimentales import *
from time import time

input = 'input files/corpus.txt'
words_frequency_1 = crear_listado_palabras_frecuencia_1(input)


start_time = time()
one_hot(input, flujo_experimental_9, words_frequency_1)
elapsed_time = time() - start_time
print("Tiempo utilizado: %.10f segundos." % elapsed_time)