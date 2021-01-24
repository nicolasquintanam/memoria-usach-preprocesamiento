from io import open
import re

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
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = remove_number(words)
    words = remove_one_character_words(words)
    
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
        linea = linea.split('####')     # linea = ["ID-123", "Este es un texto."]
        linea = linea[1]                # linea = "Este es un texto."
        linea = standardize(linea, [])  # linea = "este es un texto"
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
def obtener_numero_categoria_licitacion(categoria):
    if(categoria == 'Construcción'):
        return 1
    if(categoria == 'Salud, farmacéutica y laboratorio'):
        return 2
    if(categoria == 'Servicios y equipamiento industrial'):
        return 3
    if(categoria == 'Servicios administrativos, financieros y electrónica'):
        return 4
    else:
        return 5 # Categoría Otros.


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