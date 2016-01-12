# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:45:10 2015

@author: XuGang
"""

from __future__ import division
import json


#匹配常用语    
def parse(text,words,poss,lemmas):

    types = []
    texts = []
    
    name = '.\idiom(1).txt'
    fr1 = open(name,'r')     
    idom = json.load(fr1)[0]
    fr1.close()

    name = ".\phrasal verbs(1).txt"
    fr2 = open(name,'r')     
    phrasal_verbs = json.load(fr2)[0]
    fr2.close()
    
    name = '.\prepositional phrases(1).txt'
    fr3 = open(name,'r')     
    prepositional_phrases = json.load(fr3)[0]
    fr3.close()

    name = '.\langdao(1).txt'
    fr4 = open(name,'r')     
    langdao = json.load(fr4)[0]
    fr4.close()
    
#    print words,poss,lemmas
#    words = word_porter(text)
#    words = nltk.word_tokenize(text)
    temps = []
    for i in words:
        temp = i.lower()
        temps.append(temp)
    words = temps

    temps = []
    for i in lemmas:
        temp = i.lower()
        temps.append(temp)
    lemmas = temps
    
    lemma(types,texts,idom,phrasal_verbs,prepositional_phrases,langdao,words)

#将动词变为lemma再进行匹配    
    i = 0
    while(i < len(words)):

        if(poss[i][1][0] == "V"):
            words[i] = lemmas[i]
        i = i + 1
        
    lemma(types,texts,idom,phrasal_verbs,prepositional_phrases,langdao,words)


    
    phrase_dict = {}
    i = 0
    while(i < len(texts)):
        try:
            phrase_dict[texts[i]].add(types[i])
        except:
            phrase_dict[texts[i]] = set([types[i]])
        i = i + 1

    
    return phrase_dict

#匹配常用语内部函数
def lemma(types,texts,idom,phrasal_verbs,prepositional_phrases,langdao,words):
    
    length = len(words)
    i = 0
    while(i < length - 1):
        pair = words[i] + " " + words[i+1]

        try:
            lists1 = idom[pair]
        except:
            lists1 = []
        try:
#            print words[i],words[i+1]
            lists2 = phrasal_verbs[pair]
#            print "aaa"
        except:
            lists2 = []
        try:
            lists3 = prepositional_phrases[pair]
        except:
            lists3 = []
        try:
            lists4 = langdao[pair]
        except:
            lists4 = []
            
        lists = [lists1, lists2, lists3,lists4]
        m = 0
        for list_div in lists:
            
            if(m == 0):
                list_name = "idiom"
            elif(m == 1):
                list_name = "phrasal_verbs"
            elif(m == 2):
                list_name = "prepositional_phrases"
            else:
                list_name = "langdao"
            

            for j in list_div:  

#try..except防止字典比word长                
                try:
                    if(j == ""):
                        
                        types.append(list_name)
                        texts.append(pair)
                    
                    elif(words[i+2] == j):
    
                        string = pair + " " + words[i+2]                    
                        types.append(list_name)
                        texts.append(string)
                        
                    elif(len(j.split()) != 1):
                        
                        leng = len(j.split())
                        k = 0
        
                        final = pair
        
                        while(k < leng):
        
                            if(words[i+2+k] == j.split()[k]):
                                
                                final = final + " " + j.split()[k]
                                k = k + 1
                            else:                        
                                break
                            
                        if(k == leng):
                            types.append(list_name)
                            texts.append(final)
                except:
                    continue
            m = m + 1
        i = i + 1
        




