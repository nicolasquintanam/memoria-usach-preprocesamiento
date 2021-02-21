from time import time
import csv
import multiprocessing
import sklearn
import pandas as pd

def datasetFromFile(lineaCSV):
    try:
        listado = lineaCSV.replace('\n', '').split(';')
        map_object = map(int, listado)
        list_of_integers = list(map_object)
    except:
        print(listado)
    return list_of_integers

input_dataset = 'flujo_base_dataset.csv'
input_category = 'flujo_base_tenders-category.txt'

start_time_category = time()
categories = []
with open(input_category) as f:
    categories = f.read().splitlines()
elapsed_time = time() - start_time_category
print('Categorias en listado')
print(elapsed_time)

dataset = []
arch = open(input_dataset, 'r')
for linea in arch:
    a = linea.replace('\n', '').split(';')
    map_object = map(int, a)
    list_of_integers = list(map_object)
    dataset.append(list_of_integers)

    print(len(dataset))
print(dataset)

'''
df = pd.read_csv (input_dataset, header=None, chunksize=1, dtype='int8', delimiter=';')
for d in df:
    for i in range(len(d)):
        dataset.append(d.values[i].tolist())
        #print(d.values[i].tolist())
        print(d.reset_index().values[0].tolist())
#print(dataset)
    



start_time_dataset = time()
f1 = open(input_dataset, 'r')
lineas_dataset = f1.readlines()
pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
resultado = pool.map(datasetFromFile, lineas_dataset)
pool.close()
elapsed_time = time() - start_time_dataset
print('dataset')
print(elapsed_time)




########## PREPARAR LA DATA ##########
#Importamos los datos de la misma librería de scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
print('')
algoritmo = GaussianNB()
X_train, X_test, y_train, y_test = train_test_split(resultado, categories, test_size=0.2)
algoritmo.fit(X_train, y_train)
print('entrenado')

predictions = algoritmo.predict(X_test)
print(predictions)
'''