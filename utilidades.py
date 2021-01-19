from io import open
import re

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

            if word in lemmatization_dictionary:
                lemmatization_dictionary[word][pos]=lemma
            else:
                lemmatization_dictionary[word]={pos:lemma}
    return lemmatization_dictionary

def to_lowercase(words):
    return words.lower()

def remove_punctuation(words):
    return re.sub(r'[^\w\s]','',words)
