from representacion_vectorizada_documentos import *
from flujos_experimentales import *
from time import time

start_time = time()
one_hot('input files/corpus.txt', flujo_experimental_2)
elapsed_time = time() - start_time
print("Flujo base: %.10f seconds." % elapsed_time)