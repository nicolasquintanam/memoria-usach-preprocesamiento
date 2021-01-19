from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# Técnica 'Tokenization' del Preprocesamiento de texto.  En simples palabras, transforma el 
# el texto, que se da por parámetro, en un listado de palabras. Se obtiene de la biblioteca
# NLTK (Natural Language Toolkit).
def tokenization(words):
    return word_tokenize(words)

# Técnica 'Eliminación de Palabras Vacías'. En simples palabras, elimina las palabras que no
# son relevantes en un texto. En español, algunas palabras vacías son 'de', 'en', 'el', la',
# etc. La técnica se obtiene de la biblioteca NLTK (Natural Language Toolkit).
def remove_stopwords(word_list):
    new_word_list = word_list[:] 
    for word in word_list:
        if word in stopwords.words('spanish'): 
            new_word_list.remove(word)
    return new_word_list
