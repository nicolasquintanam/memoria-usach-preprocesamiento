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

input_dataset = 'flujo_experimental_1_dataset.csv'
input_category = 'flujo_experimental_1_tenders-category.txt'

start_time_category = time()
categories = []
with open(input_category) as f:
    categories = f.read().splitlines()
elapsed_time = time() - start_time_category
print('Categorias en listado')
print(elapsed_time)

df = pd.read_csv (input_dataset, header=None, delimiter=";", dtype=int)
print('la cantidad de filas es ' + (str(len(df.index))))
print(len(df.columns))
print(df)
'''
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