from utilidades import *
from flujos_experimentales import *
from functools import partial
from itertools import chain
import os

def one_hot_paralelize(corpus, tiene_bigrama, preprocesing_function, words_frequency_1, output_folder):
    start_time_complete = time()
    corpus_file = open(corpus, 'r')

    if not os.path.exists('output files'):
        os.makedirs('output files')

    dataset_file = open('output files/' + output_folder + '_dataset.csv', 'w')                    ## Archivo CSV que contiene el dataset puro
    abstract_file = open('output files/' + output_folder + '_abstract.txt', 'w')                  ## Archivo que indica un resumen del flujo (tiempos, cant de columnas, etc)
    one_hot_words_file = open('output files/' + output_folder + '_one-hot-words.txt', 'w')        ## Archivo con las columnas del dataset
    tenders_id_file = open('output files/' + output_folder + '_tenders-id.txt', 'w')              ## Archivo con los ID de las licitaciones
    tenders_category_file = open('output files/' + output_folder + '_tenders-category.txt', 'w')  ## Archivo con las categorías de las licitaciones
    

    textos_preprocesados = []               ## Listado de todos los textos preprocesados
    listado_id_licitaciones = []                ## ID's de las licitaciones
    categorias_licitaciones = []                ## Categoría de las licitaciones
    words_one_hot = []                          ## Palabras del Vector One-Hot
    lineas = corpus_file.readlines()            ## Listado de todas las lineas del corpus
    tokens_total_antes_preprocesamiento = 0     ## Sumatoria de todos los tokens antes del preprocesamiento
    tokens_total_despues_preprocesamiento = 0   ## Sumatoria de todos los tokens después del preprocesamiento
    tiempo_total_por_documento = 0              ## Sumatoria de todos los tiempos unitarios por documento
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

        listado_id_licitaciones.append(listado[0])                      # [0] ID de la licitación
        texto_preprocesado = listado[1].split(' ')                      # [1] --------------------------------
        if(tiene_bigrama):                                              # ------------  Texto ----------------
            texto_preprocesado = list_to_bigram(texto_preprocesado)     # ---------- preprocesado ------------
        textos_preprocesados.append(texto_preprocesado)                 # ------------------------------------
        categorias_licitaciones.append(listado[2])                      # [2] Categoría de la licitación
        tokens_total_antes_preprocesamiento += int(listado[3])          # [3] Cantidad de tokens antes del preprocesamiento
        tokens_total_despues_preprocesamiento += int(listado[4])        # [4] Cantidad de tokens después del preprocesamiento
        tiempo_total_por_documento += float(listado[5])                 # [5] Tiempo en que demoró en preprocesar el texto
        i = i + 1
        print(i)
    
    # Se crea el listado de palabras que contiene el vector one hot. Primero que todo, 
    # del listado de textos preprocesados  se transforma en un simple listado de todas
    # las palabras preprocesadas con  list(chain.from_iterable(textos_preprocesados)), 
    # luego con list(set()) se eliminan las palabras repetidas y finalmente se ordenan
    words_one_hot = sorted(list(set(list(chain.from_iterable(textos_preprocesados)))))
    
    # -------    One Hot Encoding del CSV   ------------

    j = 0
    listado_grupos_preprocesados = separarListaListas(textos_preprocesados, 1000)
    for grupo in listado_grupos_preprocesados:
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        one_hot_encoding = partial(one_hot_encoding_function, listado_palabras=words_one_hot) 
        resultado = pool.map(one_hot_encoding, grupo)

        for i in range(0, len(resultado)):
            j = j +1
            print(j)
            dataset_file.write(';'.join(resultado[i]))
            dataset_file.write('\n')
    elapsed_time_complete = time() - start_time_complete 

    # Se escribe un resumen de lo obtenido con este flujo de preprocesamiento
    abstract_file.write('La cantidad de palabras en el vector es: ' + str(len(words_one_hot)) + '\n')
    abstract_file.write('En promedio la cantidad de tokens antes del preprocesamiento: ' + str(tokens_total_antes_preprocesamiento/cantidad_documentos_corpus) + '\n')
    abstract_file.write('En promedio la cantidad de tokens después del preprocesamiento: ' + str(tokens_total_despues_preprocesamiento/cantidad_documentos_corpus) + '\n')
    abstract_file.write('El tiempo promedio que tardó cada documento es: ' + str(tiempo_total_por_documento/cantidad_documentos_corpus) + ' segundos\n')
    abstract_file.write('El tiempo que tardó el proceso completo es: ' + str(elapsed_time_complete) + ' segundos\n')

    # Se escribe en un archivo todas las palabras del vector one hot.
    if(tiene_bigrama):
        one_hot_words_file.write('\n'.join(map(str, words_one_hot)))
    else:
        one_hot_words_file.write('\n'.join(words_one_hot))

    # Se escribe en un archivo todas las licitaciones preprocesadas
    tenders_id_file.write('\n'.join(listado_id_licitaciones))

    # Se escribe en un archivo todas las categorías de las licitaciones preprocesadas
    tenders_category_file.write('\n'.join(categorias_licitaciones))

    abstract_file.close()
    one_hot_words_file.close()
    tenders_id_file.close()
    tenders_category_file.close()
    dataset_file.close()
    corpus_file.close()
    


def one_hot_encoding_function(texto, listado_palabras):
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
