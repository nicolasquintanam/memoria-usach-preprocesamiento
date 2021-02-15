from utilidades import *
from flujos_experimentales import *
from functools import partial
from itertools import chain

def one_hot_paralelize(corpus, tiene_bigrama, preprocesing_function, words_frequency_1):
    start_time_complete = time()
    corpus_file = open(corpus, 'r')

    dataset_file = open('output files/dataset.csv', 'w')            ## Archivo CSV que contiene el dataset puro
    abstract_file = open('output files/abstract.txt', 'w')          ## Archivo que indica un resumen del flujo (tiempos, cant de columnas, etc)
    one_hot_words = open('output files/one-hot-words.txt', 'w')     ## Archivo con las columnas del dataset
    tenders_id = open('output files/tenders-id.txt', 'w')           ## Archivo con los ID de las licitaciones
    

    textos_preprocesados = []               ## Listado de todos los textos preprocesados
    listado_id_licitaciones = []                ## ID's de las licitaciones
    categorias_licitaciones = []                ## Categoría de las licitaciones
    words_one_hot = []                          ## Palabras del Vector One-Hot
    tiempos_documento = []                      ## Listado de los tiempos que demora cada texto en ser preprocesado
    tokens_antes_preprocesamiento = []          ## Cantidad de tokens antes del preprocesamiento
    tokens_despues_preprocesamiento = []        ## Cantidad de tokens después del preprocesamiento
    lineas = corpus_file.readlines()            ## Listado de todas las lineas del corpus
    cantidad_documentos_corpus = len(lineas)    ## Cantidad de documentos en el corpus
    
    ## Se preprocesa cada documento, es decir, cada linea en la variable
    ## 'lineas', utilizando paralelismo. 
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    preprocesamiento_por_documento = partial(preprocesar_documento, preprocesing_function=preprocesing_function, words_frequency_1=words_frequency_1, tiene_bigram=tiene_bigrama) # prod_x has only one argument x (y is fixed to 10)
    resultado = pool.map(preprocesamiento_por_documento, lineas)
    # La variable resultado, por cada texto trae lo siguiente separado por '####':
    #   -   [0] ID de la licitación
    #   -   [1] Texto preprocesado
    #   -   [2] Categoría de la licitación
    #   -   [3] Cantidad de tokens antes del preprocesamiento
    #   -   [4] Cantidad de tokens después del preprocesamiento
    #   -   [5] Tiempo que demoró en preprocesar el texto

    i = 0
    for texto in resultado:
        listado = texto.split('####') 
        
        listado_id_licitaciones.append(listado[0])
        texto_preprocesado = listado[1]
        if(tiene_bigrama):
            texto_preprocesado = list_to_bigram(texto_preprocesado.split(' '))
        
        categorias_licitaciones.append(listado[2])
        tokens_antes_preprocesamiento.append(listado[3])
        tokens_despues_preprocesamiento.append(listado[4])
        tiempos_documento.append(listado[5])

        if(type(texto_preprocesado) != list):
            texto_preprocesado = texto_preprocesado.split(' ')
        textos_preprocesados.append(texto_preprocesado)
        i = i + 1
        print(i)
    
    words_one_hot = sorted(list(set(list(chain.from_iterable(textos_preprocesados)))))
        
    # Se crea una nueva variable de palabras del vector OneHot que almacene las palabras 
    # del vector OneHot, pero solo aquellas que tengan frecuencia > 1 y frecuencia menor
    # a la cantidad total de documentos,    esto porque si una palabra está en todos los
    # documentos, no sirve para clasificar.
    ##ESte quizś se puede optimizar solamente escribiendo y no linea por linea.
    new_words_one_hot = []
    for i in range(len(words_one_hot)):
        new_words_one_hot.append(words_one_hot[i])
        dataset_file.write(';' + str(words_one_hot[i]))            
        
    dataset_file.write(';licitacion_categoria')
    dataset_file.write('\n')
    #Con esto ya se encuentra listo el header del CSV
    #   | word1 | word2 | word3 | word4 | ...... | wordn | licitacion_categoria
    abstract_file.write('La cantidad de palabras en el vector es: ' + str(len(new_words_one_hot)) + '\n')


    tokens_total_antes_preprocesamiento = 0
    tokens_total_despues_preprocesamiento = 0
    tiempo_total_por_documento = 0

    print('antes es: ' + str(len(textos_preprocesados)))
    lt_preprocesados = separarListaListas(textos_preprocesados, 1000)
    print('después es: ' + str(len(lt_preprocesados)))
    j = 0
    for grupo in lt_preprocesados:
        
        hola = []
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        prod_y=partial(funcionnn2, listado_palabras=new_words_one_hot) # prod_x has only one argument x (y is fixed to 10)
        hola = pool.map(prod_y, grupo)

        for i in range(0, len(hola)):
            print(i)
            print(i+j)
            dataset_file.write(str(listado_id_licitaciones[i+j]))
            dataset_file.write(';')
            dataset_file.write(';'.join(hola[i]))
            dataset_file.write(';' + categorias_licitaciones[i+j])
            dataset_file.write('\n')

            tiempo_total_por_documento += float(tiempos_documento[i+j])
            tokens_total_antes_preprocesamiento += int(tokens_antes_preprocesamiento[i+j])
            tokens_total_despues_preprocesamiento += int(tokens_despues_preprocesamiento[i+j])
        j = j + 1000
     
    
    abstract_file.write('En promedio la cantidad de tokens antes del preprocesamiento: ' + str(tokens_total_antes_preprocesamiento/len(tokens_antes_preprocesamiento)) + '\n')
    abstract_file.write('En promedio la cantidad de tokens después del preprocesamiento: ' + str(tokens_total_despues_preprocesamiento/len(tokens_despues_preprocesamiento)) + '\n')
    abstract_file.write('El tiempo promedio que tardó cada documento es: ' + str(tiempo_total_por_documento/len(tiempos_documento)) + ' segundos\n')
    elapsed_time_complete = time() - start_time_complete
    abstract_file.write('El tiempo que tardó el proceso completo es: ' + str(elapsed_time_complete) + ' segundos\n')

    abstract_file.close()
    dataset_file.close()
    corpus_file.close()


def funcionnn2(texto, listado_palabras):
    one_hot = []
    for palabra in listado_palabras:
        if(palabra in texto):
            one_hot.append('1')
        else:
            one_hot.append('0')
    return one_hot

def preprocesar_documento(linea, preprocesing_function, words_frequency_1, tiene_bigram):
    lista = linea.split('####')
    cantidad_tokens_antes_preprocesamiento = len(lista[1].split(' '))
    start_time_for_each_document = time()
    preprocesado = preprocesing_function(standardize(lista[1], words_frequency_1))
    elapsed_time = time() - start_time_for_each_document
    cantidad_tokens_despues_preprocesamiento = len(preprocesado)
    if(lista[0] == '3890-106-L119'):
        print('-- Preprocesado 15,3% (5.000 licitaciones) ----')
    
    if(lista[0] == '2385-27-LE19'):
        print('-- Preprocesado 30,7% (10.000 licitaciones) ----')
    
    if(lista[0] == '2422-566-LE19'):
        print('-- Preprocesado 46,1% (15.000 licitaciones) ----')

    if(lista[0] == '744835-8-L120'):
        print('-- Preprocesado 61,4% (20.000 licitaciones) ----')
    
    if(lista[0] == '2450-59-L120'):
        print('-- Preprocesado 76,8% (25.000 licitaciones) ----')

    if(lista[0] == '2827-14-LE20'):
        print('-- Preprocesado 92,2% (30.000 licitaciones) ----')


    new_preprocesado = list(set(preprocesado))
    
    
    if(tiene_bigram):
        new_preprocesado = bigram_to_list(new_preprocesado)

    resultado = lista[0] + '####' + ' '.join(new_preprocesado) + '####' + lista[2].replace('\n', '') + '####' + str(cantidad_tokens_antes_preprocesamiento) + '####' + str(cantidad_tokens_despues_preprocesamiento) + '####' + str(elapsed_time)
    return resultado
