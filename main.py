from representacion_vectorizada_documentos import *
from flujos_experimentales import *
from time import time

input = 'input files/corpus.txt'

start_time = time()
one_hot(input, flujo_base)
elapsed_time = time() - start_time
print("Tiempo utilizado: %.10f segundos." % elapsed_time)