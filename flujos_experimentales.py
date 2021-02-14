from tecnicas_preprocesamiento_texto import *
from utilidades import *
import pickle
import os.path
from os import path

#region Lemmatization Dictionary 
lemmatization_dictionary = {}
if(path.exists("linguistic data/word_lemma_dict.pkl")):
    with open('linguistic data/word_lemma_dict.pkl', 'rb') as f:
        lemmatization_dictionary = pickle.load(f)
else:
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/verbos.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/verbos-chile.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/adjetivos.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/adjetivos-chile.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/sustantivos.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/sustantivos-chile.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/adverbios.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/adverbios-chile.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/interjecciones-chile.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/gentilicios-chile.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/otros.txt')
    lemmatization_dictionary = create_lemmatization_dictionary(lemmatization_dictionary, 'linguistic data/otros-chile.txt')
    pickle.dump(dictionary, open('linguistic data/word_lemma_dict.pkl','wb'))
#endregion

#region NER Dictionary
ner_dictionary = {}
ner_dictionary = create_ner_dictionary(ner_dictionary, 'linguistic data/diccionario_ner.txt')
#endregion

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
    word_list = lemmatization(word_list, lemmatization_dictionary)
    return word_list

def flujo_experimental_3(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, lemmatization_dictionary)
    word_list = ngram(word_list, 2)
    return word_list

def flujo_experimental_4(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = ner(word_list, ner_dictionary)
    word_list = stemming(word_list)
    word_list = ngram(word_list, 2)
    return word_list

def flujo_experimental_5(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = ner(word_list, ner_dictionary)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, lemmatization_dictionary)
    return word_list

def flujo_experimental_6(words):
    word_list = tokenization(words)
    word_list = remove_stopwords(word_list)
    word_list = ner(word_list, ner_dictionary)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, lemmatization_dictionary)
    word_list = ngram(word_list, 2)
    return word_list

def flujo_experimental_7(words):
    word_list = tokenization(words)
    word_list = ner(word_list, ner_dictionary)
    word_list = remove_stopwords(word_list)
    word_list = stemming(word_list)
    return word_list

def flujo_experimental_8(words):
    word_list = tokenization(words)
    word_list = ner(word_list, ner_dictionary)
    word_list = remove_stopwords(word_list)
    word_list = lemmatization(word_list)
    return word_list

def flujo_experimental_9(words):
    word_list = tokenization(words)
    word_list = ner(word_list, ner_dictionary)
    word_list = remove_stopwords(word_list)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, lemmatization_dictionary)
    return word_list

def flujo_experimental_10(words):
    word_list = tokenization(words)
    word_list = ner(word_list, ner_dictionary)
    word_list = remove_stopwords(word_list)
    word_list = pos_tagging(word_list)
    word_list = lemmatization(word_list, lemmatization_dictionary)
    word_list = ngram(word_list, 2)
    return word_list