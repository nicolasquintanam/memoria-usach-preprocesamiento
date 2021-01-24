from utilidades import *

# Permite crear el vector one hot y exportarlo a un archivo CSV.
def one_hot(corpus, preprocessing_function, words_frequency_1):
    archivo_salida = open('output files/dataset.csv', 'w')
    archivo = open(corpus, 'r')
    vector = []                     # Vector OneHot como array
    words_one_hot = []              # Palabras que contiene el vector OneHot
    words_one_hot_count = []        # Cantidad de veces que se repite las palabras del vector OneHot
    licitaciones_id = []            # Listado de los ID's de las licitaciones
    categorias_licitaciones = []    # Listado de categorías de las licitaciones

    cantidad_lineas = 0
    for linea in archivo:
                                                                    # linea = "ID-123####Este es un texto.####Construccion"
        linea = linea.split('####')                                 # linea = ["ID-123", "Este es un texto.", "Construccion"]
        licitaciones_id.append(linea[0])
        categorias_licitaciones.append(linea[2].replace('\n', ''))
        linea = linea[1]                                            # linea = "Este es un texto.
        linea = standardize(linea, words_frequency_1)               # linea = "este es un texto"

        # Comienza el flujo de preprocesamiento de texto por cada línea, es decir, cada documento.
        preprocessing_line = preprocessing_function(linea)

        # Se eliminan los repetidos en preprocessing_line
        new_preprocessing_line = []
        for word in preprocessing_line:
            if(word not in new_preprocessing_line):
                new_preprocessing_line.append(word)
        preprocessing_line = new_preprocessing_line

        #Se añade al vector OneHot el documento preprocesado
        vector.append(preprocessing_line)

                          
        for word in preprocessing_line:             # Aquí, se van agregando el listado de palabras del vector OneHot, y a la vez,  
            if word not in words_one_hot:           # se va agregando la cantidad de veces que se repite en los documentos, con el  
                words_one_hot_count.append(1)       # fin de no considerar aquellas palabras que tienen frecuencia 1.      
                words_one_hot.append(word)          # Ej:              
            else:                                   #   -   words_one_hot =         ["este", "ser", "un", "texto"]                                      
                indice = words_one_hot.index(word)  #   -   words_one_hot_count =   [4, 2, 5, 1]                                          
                words_one_hot_count[indice] += 1    # Con el ejemplo,  quiere decir que la palabra "texto" se encuentra solo en un                                           
        cantidad_lineas += 1                        # documento, por lo tanto, no tiene relevancia en el vector OneHot.                                                   
    


    new_words_one_hot = []
    if(cantidad_lineas > 1):
        # Se crea una nueva variable de palabras del vector OneHot que almacene las palabras 
        # del vector OneHot, pero solo aquellas que tengan frecuencia > 1 y frecuencia menor
        # a la cantidad total de documentos,    esto porque si una palabra está en todos los
        # documentos, no sirve para clasificar.
        contador = 0
        for word in words_one_hot:
            if(words_one_hot_count[contador] > 1 and words_one_hot_count[contador] < cantidad_lineas):
                new_words_one_hot.append(word)
                archivo_salida.write(';' + str(word))
            contador += 1
    else:
        new_words_one_hot = words_one_hot
        for word in new_words_one_hot:
            archivo_salida.write(';' + str(word))

    archivo_salida.write(';licitacion_categoria')
    archivo_salida.write('\n')
    i = 0
    for document in vector:
        archivo_salida.write(str(licitaciones_id[i]))
        for word in new_words_one_hot:
            if(word in document):
                archivo_salida.write(';1')
            else:
                archivo_salida.write(';0')
        archivo_salida.write(';' + str(obtener_numero_categoria_licitacion(categorias_licitaciones[i])))
        archivo_salida.write('\n')
        i = i + 1
    archivo_salida.close()
    archivo.close()
    return vector