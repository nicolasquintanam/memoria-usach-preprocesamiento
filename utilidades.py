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
def standardize(words):
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = remove_number(words)
    words = remove_one_character_words(words)
    return words

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