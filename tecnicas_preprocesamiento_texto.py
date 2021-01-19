from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk import SnowballStemmer
import es_core_news_sm


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

# Técnica 'Stemming' del Preprocesamiento de texto. En simples palabras, transforma cada pala-
# bra de un listado,  en la raíz sin las formas gramaticales, en otras palabras se trunca cada
# palabra. Por ejemplo: [compré, compró, compraste, comprarás, comprar, compra] -> [compr]
def stemming(word_list):
    spanishstemmer = SnowballStemmer('spanish')
    return [spanishstemmer.stem(token) for token in word_list]

# Técnica 'Etiquetado Gramatical'. Permite asignar a cada palabra del listado, una etiqueta mor-
# fosintáctica, es decir, su categoría gramatical.  Si la palabra es un verbo, adverbio, sustan-
# tivo, etc.
def pos_tagging(word_list):
    nlp = es_core_news_sm.load()
    doc = nlp(' '.join(word_list))
    new_word_list = []
    for word in doc:
        new_word_list.append((word.text, word.pos_))
    return new_word_list

# Técnica 'N-Gramas'. Permite representar una secuencia de n palabras contiguas en el texto. Para 
# transformarlo en un listado. 
# Ejemplo con n=2 para [hola, como, estas, bien] -> [(hola, como), (como, estas), (estas, bien)].
def ngram(word_list, n):
    return list(ngrams(word_list, n))

# Técnica 'Lematización'.  Permite transformar cada palabra de un listado, en la versión como apa-
# rece en el diccionario. Ejemplo: [corrí, correré, corriendo] -> [correr].  Cabe destacar, que la 
# Lematización en la biblioteca Spacy, para el español, no diferencia el etiquetado gramatical, es 
# decir, no diferencia si la palabra 'vino' es del verbo 'venir', o 'vino' de bebida alcohólica.
# Para solucionar esto, se puede utilizar la técnica POS Tagging antes de la Lematización, y utili-
# zar un diccionario que indique la palabra, el lema y el etiquetado gramatical.
def lemmatization(word_list, dictionary=None):
    #Lematización sin información de Etiquetado Gramatical
    if(dictionary is None):
        nlp = es_core_news_sm.load()
        doc = nlp(' '.join(word_list))
        new_word_list = []
        for word in doc:
            new_word_list.append(word.lemma_)
        return new_word_list
    # Lematización con información de Etiquetado Gramatical, solo se puede utilizar
    # si antes, se utiliza la técnica POS Tagging, y se indica por parámetro el di-
    # ccionario gramatical.
    else:
        new_word_list = []
        for word in word_list:
            w = word[0]
            pos = word[1]
            if(pos == 'PROPN'):
                new_word_list.append(w)
            else:
                if w in dictionary:
                    if pos in dictionary[w]:
                        new_word_list.append(dictionary[w][pos])
                    else:
                        print('no está el ' + pos + ' del ' + w)
                else:
                    print('no está ' + w)
        return new_word_list

def ner(word_list):
    return word_list
