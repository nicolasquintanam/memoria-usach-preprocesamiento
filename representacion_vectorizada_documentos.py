from utilidades import *

# Permite crear el vector one hot y exportarlo a un archivo CSV.
def one_hot(corpus, preprocessing_function):
    archivo_salida = open('output files/dataset.csv', 'w')
    archivo = open(corpus, 'r')
    vector = []
    words_one_hot = []
    for linea in archivo:
        linea = standardize(linea)
        preprocessing_line = preprocessing_function(linea)
        vector.append(preprocessing_line)
        for word in preprocessing_line:
            if word not in words_one_hot:
                words_one_hot.append(word)
                archivo_salida.write(str(word) + ';')
    archivo_salida.write('\n')
    
    for document in vector:
        for word in words_one_hot:
            if(word in document):
                archivo_salida.write('1;')
            else:
                archivo_salida.write('0;')
        archivo_salida.write('\n')
    archivo_salida.close()
    archivo.close()
    return vector