from tecnicas_preprocesamiento_texto import *
from utilidades import *
import pickle
import os.path
from os import path

print("Creando diccionario de lematización")
dictionary = {}
if(path.exists("linguistic data/word_lemma_dict.pkl")):
    with open('linguistic data/word_lemma_dict.pkl', 'rb') as f:
        dictionary = pickle.load(f)
else:
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/verbos.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/verbos-chile.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/adjetivos.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/adjetivos-chile.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/sustantivos.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/sustantivos-chile.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/adverbios.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/adverbios-chile.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/interjecciones-chile.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/gentilicios-chile.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/otros.txt')
    dictionary = create_lemmatization_dictionary(dictionary, 'linguistic data/otros-chile.txt')
    pickle.dump(dictionary, open('linguistic data/word_lemma_dict.pkl','wb'))
print("Diccionario de lematización creado!\n")

def flujo_base(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = stemming(word_list)
    return word_list

def flujo_experimental_1(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = stemming(word_list)
    word_list = ngram(word_list, 2)
    return word_list

def flujo_experimental_2(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, dictionary)
    return word_list

def flujo_experimental_3(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, dictionary)
    word_list = ngram(word_list, 2)
    return word_list

def flujo_experimental_4(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = ner(word_list)
    word_list = stemming(word_list)
    word_list = ngram(word_list, 2)
    return word_list

def flujo_experimental_5(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = ner(word_list)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, dictionary)
    return word_list

def flujo_experimental_6(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = ner(word_list)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, dictionary)
    word_list = ngram(word_list, 2)
    return word_list

def flujo_experimental_7(words):
    word_list = tokenization(words)
    word_list = ner(word_list)
    word_list = remove_stopwords(word_list)
    word_list = stemming(word_list)
    return word_list

def flujo_experimental_8(words):
    word_list = tokenization(words)
    word_list = ner(word_list)
    word_list = remove_stopwords(word_list)
    word_list = lemmatization(word_list)
    return word_list

def flujo_experimental_9(words):
    word_list = tokenization(words)
    word_list = ner(word_list)
    word_list = remove_stopwords(word_list)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, dictionary)
    return word_list

def flujo_experimental_10(words):
    word_list = tokenization(words)
    word_list = ner(word_list)
    word_list = remove_stopwords(word_list)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, dictionary)
    word_list = ngram(word_list, 2)
    return word_list