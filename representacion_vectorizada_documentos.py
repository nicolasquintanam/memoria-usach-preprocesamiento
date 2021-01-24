from utilidades import *

# Permite crear el vector one hot y exportarlo a un archivo CSV.
def one_hot(corpus, preprocessing_function):
    archivo_salida = open('output files/dataset.csv', 'w')
    archivo = open(corpus, 'r')
    vector = []
    words_one_hot = []
    licitaciones_id = []
    i = 0
    for li in archivo:
        sppliteado = li.split('####')
        id_licitacion = sppliteado[0]
        licitaciones_id.append(id_licitacion)
        linea = sppliteado[1]
        linea = standardize(linea)
        preprocessing_line = preprocessing_function(linea)
        print('documento '+ str(i) + ' preprocesado')
        vector.append(preprocessing_line)
        for word in preprocessing_line:
            if word not in words_one_hot:
                words_one_hot.append(word)
                archivo_salida.write(';' + str(word))
        i = i + 1
    archivo_salida.write('\n')
    i = 0
    len(vector)
    for document in vector:
        archivo_salida.write(str(licitaciones_id[i]))
        for word in words_one_hot:
            if(word in document):
                archivo_salida.write(';1')
            else:
                archivo_salida.write(';0')
        archivo_salida.write('\n')
        print('\n\n\n\n')
        i = i + 1
    archivo_salida.close()
    archivo.close()
    return vector