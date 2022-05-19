# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:22:14 2022

@author: young
"""
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from textblob import TextBlob, Word
from nltk.corpus import stopwords

def lem(a):   
    sent = TextBlob(a)
    result = " ".join([w.lemmatize() for w in sent.words])
    return result   #lemmentization

def process_text(a):
    a = str(re.sub("\S*\d\S*", "", a).strip()) 
    a = a.lower()    
    a = re.sub(r"[^a-zA-Z0-9]"," ",a) #특수문자 제거
    a = re.sub("([^\x00-\x7F])+","",a) #영어이외제거    
    a = re.sub("(.)\\1{3,}", "\\1", a) #긴 반복문 제거
    a = shortword.sub(' ', a)    #짧은 단어 제거        
        
    tokenizer = TreebankWordTokenizer()
    # tokenize texts
    tokens = tokenizer.tokenize(a)
    
    
    result = []
    for b in tokens:
        b = shortword.sub(' ', b)    #짧은 단어 제거  
        if b not in stop_words:  #stopwords 제거
            result.append(b)   
    
    return result

