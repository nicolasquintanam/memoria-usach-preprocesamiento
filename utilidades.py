from io import open
import re
from time import time
import pandas as pd
import numpy as np
import multiprocessing
from joblib import Parallel, delayed

# Permite crear un diccionario para la lematización. Este diccionario contiene información
# de la palabra, su forma gramatical y su lema.   Por lo tanto, por parámetro se le indica
# el diccionario, al principio se le debe indicar vacío, y el archivo que contiene las pa-
# labras, con su forma gramatical y su lema. Se le indica por parámetro el diccionario pa-
# ra que luego de agregar el primer archivo, se le puedan ir agregando otros archivos, con
# otras palabras y otras formas gramaticales.
def create_lemmatization_dictionary(lemmatization_dictionary, file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.read()
    lines = lines.replace('\ufeff','').split("\n")
    for line in lines:
        aux_list = line.split(' ')
        if(len(aux_list) == 3):
            word = aux_list[0]
            lemma = aux_list[1]
            pos = ''
            if(aux_list[2][0] == 'V'):
                pos = 'VERB'
            if(aux_list[2][0] == 'A'):
                pos = 'ADJ'
            if(aux_list[2][0] == 'R'):
                pos = 'ADV'
            if(aux_list[2][0] == 'N'):
                pos = 'NOUN'
            if(aux_list[2][0] == 'S'):
                pos = 'ADP'
            if(aux_list[2][0] == 'C'):
                pos = 'CONJ'
            if(aux_list[2][0] == 'D'):
                pos = 'DET'
            if(aux_list[2][0] == 'I'):
                pos = 'INT'
            if(aux_list[2][0] == 'P'):
                pos = 'PRON'

            if word in lemmatization_dictionary:
                lemmatization_dictionary[word][pos]=lemma
            else:
                lemmatization_dictionary[word]={pos:lemma}
    return lemmatization_dictionary

# Permite estandarizar el texto antes de ser utilizado por las técnicas de preprocesamiento
# de texto. Esta estandarización consta de transformar el texto a minúsculas, eliminar pun-
# tos, comas y puntuaciones en general,  eliminar números y eliminar palabras que contienen 
# solo una letra.
def standardize(words, listado_palabras_frecuencia_1):
    words = words.replace('\n', ' ')
    words = words.replace('\t', ' ')
    words = words.replace('\r', ' ')
    words = words.replace('_', ' ')
    # Si viene vacío el listado de palabras con frecuencia 1, no considerar.
    if(listado_palabras_frecuencia_1 == []):
        return words
    # Si no viene vacío, eliminar las palabras contenidas en el listado de palabras con fre-
    # cuencia 1.
    else:
        return ' '.join([word for word in words.split(' ') if (word not in listado_palabras_frecuencia_1)])

# Transforma todo el texto a minúsculas.
def to_lowercase(words):
    return words.lower()

# Elimina puntuaciones de un texto.
def remove_punctuation(words):
    return re.sub(r'[^\w\s]','',words)

# Elimina los números de un texto.
def remove_number(words):
    return ''.join([i for i in words if not i.isdigit()])

# Elimina las palabras que tienen solo un caracter.
def remove_one_character_words(words):
    word_list = words.split(' ')
    return ' '.join([i for i in word_list if (len(i) > 1)])

# A partir del archivo corpus, se obtiene un listado de todas las palabras que no se repiten,
# es decir, tienen frecuencia uno, durante todo el corpus. 
def crear_listado_palabras_frecuencia_1(input):
    diccionario_contador_palabras = {}
    archivo_entrada = open(input, 'r')
    
    i = 0
    for linea in archivo_entrada:
                                            # linea = "ID-123####Este es un texto."
        linea = linea.split('####')         # linea = ["ID-123", "Este es un texto."]
        linea = standardize(linea[1], [])   # linea = "Este es un texto."
        linea = linea.split(' ')        # linea = ["este", "es", "un", "texto"]
        # almacenar lo mismo que en 'linea' pero sin palabras repetidas
        new_linea = []      
        for palabra in linea:
            if palabra not in new_linea:
                new_linea.append(palabra)

        # se va contando, por cada palabra en el corpus, la cantidad de veces que aparece
        for word in new_linea:
            if word in diccionario_contador_palabras: 
                diccionario_contador_palabras[word] += 1
            else:                                     
                diccionario_contador_palabras[word] = 1
        i += 1
    if(i == 1):
        return []
    else:
        # se crea un listado que almacena todas las palabras con frecuencia 1,
        # con el fin de no considerarlas, porque no influye en el resultado.
        listado_palabras_frecuencia_1 = []
        for palabra in diccionario_contador_palabras:
            if(diccionario_contador_palabras[palabra] == 1):
                listado_palabras_frecuencia_1.append(palabra)
        return listado_palabras_frecuencia_1

# Obtiene el identificador de la categoría de la licitación.
def obtener_numero_categoria_licitacion(categoria, category_dictionary):
    category = ''
    categoria = categoria.replace('  ', ' ').strip()
    
    if(categoria in category_dictionary):
        category = category_dictionary[categoria]
    if(category == 'Construcción'):
        return 1
    if(category == 'Salud, farmacéutica y laboratorio'):
        return 2
    if(category == 'Servicios y equipamiento industrial'):
        return 3
    if(category == 'Servicios administrativos, financieros y electrónica'):
        return 4
    else:
        return 5 #Categoría Otros

def eliminar_repetidos(listado):
    nuevo_listado = []
    for elemento in listado:
        if(elemento not in nuevo_listado):
            nuevo_listado.append(elemento)
    return nuevo_listado

# Crea un diccionario de Named Entity Recognition a partir de un archivo.
def create_ner_dictionary(ner_dictionary, file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.read()
    lines = lines.replace('\ufeff','').split("\n")
    for line in lines:
        aux_list = line.split(' ## ')
        if(len(aux_list) == 2):
            word = aux_list[0]
            replace = aux_list[1]
            if word in ner_dictionary:
                ner_dictionary[word]=replace
            else:
                ner_dictionary[word]={replace}
    return ner_dictionary

# Permite crear un diccionario de categorías, en donde se indica la categoría
# original y retorna la categoría definitiva, reduciendo así, las 56 categor-
# ías a solo 5.
def create_category_dictionary():
    category_dictionary = {}

    category = "Construcción"
    category_dictionary["Artículos para estructuras obras y construcciones"] = category
    category_dictionary["Maquinaria para construcción y edificación"] = category
    category_dictionary["Servicios de construcción y mantenimiento"] = category

    category = "Salud, farmacéutica y laboratorio"
    category_dictionary["Equipamiento para laboratorios"] = category
    category_dictionary["Equipamiento y suministros médicos"] = category
    category_dictionary["Medicamentos y productos farmacéuticos"] = category
    category_dictionary["Salud servicios sanitarios y alimentación"] = category

    category = "Servicios y equipamiento industrial"
    category_dictionary["Artículos de fabricación y producción"] = category
    category_dictionary["Combustibles lubricantes y anticorrosivos"] = category
    category_dictionary["Equipamiento para el acondicionamiento distribución y filtrado de fluidos"] = category
    category_dictionary["Equipamiento para manejo y estiba de materiales"] = category
    category_dictionary["Herramientas y maquinaria en general"] = category
    category_dictionary["Maquinaria para fabricación y transformación industrial"] = category
    category_dictionary["Maquinaria para minería y perforación"] = category
    category_dictionary["Maquinarias equipos y suministros para la industria de servicios"] = category
    category_dictionary["Productos químicos industriales"] = category
    category_dictionary["Resinas cauchos espumas y elastómeros"] = category
    category_dictionary["Servicios de limpieza industrial"] = category
    category_dictionary["Servicios de perforación de minería petróleo y gas"] = category
    category_dictionary["Servicios de producción y fabricación industrial"] = category
    category_dictionary["Servicios de transporte almacenaje y correo"] = category
    category_dictionary["Vehículos y equipamiento en general"] = category

    category = "Servicios administrativos, financieros y electrónica"
    category_dictionary["Consultoria"] = category
    category_dictionary["Equipos accesorios y suministros de oficina"] = category
    category_dictionary["Organizaciones y consultorías políticas demográficas económicas sociales y de administración pública"] = category
    category_dictionary["Productos de papel"] = category
    category_dictionary["Productos impresos y publicaciones"] = category
    category_dictionary["Servicios financieros pensiones y seguros"] = category
    category_dictionary["Servicios profesionales administrativos y consultorías de gestión empresarial"] = category
    category_dictionary["Artículos de electrónica"] = category
    category_dictionary["Artículos eléctricos y de iluminación"] = category
    category_dictionary["Equipos y suministros de imprenta fotográficos y audiovisuales"] = category
    category_dictionary["Maquinaria para generación y distribución de energía"] = category
    category_dictionary["Muebles accesorios electrodomésticos y productos electrónicos"] = category
    category_dictionary["Servicios basados en ingeniería ciencias sociales y tecnología de la información"] = category
    category_dictionary["Servicios editoriales de diseño publicidad gráficos y artistas"] = category
    category_dictionary["Tecnologías de la información telecomunicaciones y radiodifusión"] = category

    category = "Otros"
    category_dictionary["Alimentos bebidas y tabaco"] = category
    category_dictionary["Artículos para plantas y animales"] = category
    category_dictionary["Educación formación entrenamiento y capacitación"] = category
    category_dictionary["Equipos suministros y accesorios deportivos y recreativos"] = category
    category_dictionary["Equipos y suministros de defensa orden público protección y seguridad"] = category
    category_dictionary["Equipos y suministros de limpieza"] = category
    category_dictionary["Instrumentos musicales juegos juguetes artesanías y materiales educativos"] = category
    category_dictionary["Maquinaria para agricultura pesca y silvicultura"] = category
    category_dictionary["Muebles y mobiliario"] = category
    category_dictionary["Organizaciones sociales laborales y clubes"] = category
    category_dictionary["Productos derivados de minerales plantas y animales"] = category
    category_dictionary["Productos para relojería joyería y gemas"] = category
    category_dictionary["Ropa maletas y productos de aseo personal"] = category
    category_dictionary["Servicios agrícolas pesqueros forestales y relacionados con la fauna"] = category
    category_dictionary["Servicios básicos y de información pública"] = category
    category_dictionary["Servicios de cuidado personal y domésticos"] = category
    category_dictionary["Servicios de defensa nacional orden público y seguridad"] = category
    category_dictionary["Servicios de Viajes alimentación alojamiento y entretenimiento"] = category
    category_dictionary["Servicios medioambientales"] = category

    return category_dictionary

def transformNERLabel(tag):
    if(tag == 'PERSON'):
        return 'persona'
    if(tag == 'NORP'):
        return 'entidad'
    if(tag == 'FAC' or tag == 'GPE' or tag == 'LOC'):
        return 'lugar'
    if(tag=='LANGUAGE'):
        return 'lenguaje'
    if(tag=='DATE'):
        return 'fecha'
    if(tag == 'TIME'):
        return 'hora'
    if(tag == 'ORG'):
        return 'organización'
    return tag

def bigram_to_list(bigram):
    lista = []
    for element in bigram:
        lista.append(element[0])
        lista.append(element[1])
    return lista

def list_to_bigram(lista):
    bigram = []
    for i in range(0, len(lista), 2):
        bigram.append(tuple(lista[i:i+2]))
    return bigram

def separarListaListas(lista, n):
    new_lista = []
    for i in range(0, len(lista), n):
        new_lista.append(lista[i:i+n])
    return new_lista