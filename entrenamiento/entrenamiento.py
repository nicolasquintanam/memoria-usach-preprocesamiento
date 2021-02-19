from time import time
import csv
import multiprocessing


def datasetFromFile(lineaCSV):
    return lineaCSV.replace('\n', '').split(';')

input_dataset = 'flujo_base_dataset.csv'
input_category = 'flujo_base_tenders-category.txt'

start_time_category = time()
categories = []
with open(input_category) as f:
    categories = f.read().splitlines()
elapsed_time = time() - start_time_category
print('Categorias en listado')
print(elapsed_time)

start_time_dataset = time()
f1 = open(input_dataset, 'r')
lineas_dataset = f1.readlines()
pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
resultado = pool.map(datasetFromFile, lineas_dataset)
pool.close()
elapsed_time = time() - start_time_dataset
print('dataset')
print(elapsed_time)


'''
for i in range(len(lineas_dataset)):
    linea_category = lineas_category[i].replace('\n', '')
    categorias.append(linea_category)
    print(linea_category)

with open(input_dataset, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

#print(data)

########## PREPARAR LA DATA ##########
#Importamos los datos de la misma librería de scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
algoritmo = GaussianNB()
X_train, X_test, y_train, y_test = train_test_split(data, categorias, test_size=0.2)
algoritmo.fit(X_train, y_train)
print('entrenado')
'''
