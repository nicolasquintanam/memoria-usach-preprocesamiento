from tecnicas_preprocesamiento_texto import *
from utilidades import *

text = ''
dictionary = {}
dictionary = create_lemmatization_dictionary(dictionary, 'archivo/verbos.txt')
dictionary = create_lemmatization_dictionary(dictionary, 'archivo/adjetivos.txt')
dictionary = create_lemmatization_dictionary(dictionary, 'archivo/sustantivos.txt')

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
