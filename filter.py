#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import collections
import pprint
reload(sys)
sys.setdefaultencoding('utf-8')

letters = ['а', 'ә', 'б', 'в', 'г', 'ғ', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'қ', 
            u'л', 'м', 'н', 'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ұ', 'ү', 'ф', 
            u'х', 'ц', 'ч', 'ш', 'ы', 'і', 'э', 'ю', 'я']
            
word = []
index = 0
   
for i in letters:
    with open('parsed-words/letter-'+i+'.json') as data_file:    
        data = json.load(data_file)
    
    for i in range(len(data)):
        dict_ = collections.OrderedDict()
        index+=1
        dict_["id"] = index
        #dict_["word"] = data[i]['word'].encode("utf-8")
        #dict_["len"] = len(data[i]['word'])
        #word.append(dict_)
        
        w = data[i]['translation'].replace("гл. ", "").replace("уст. ", "").replace("ар. ", "")
        if "1)" in w:
            start = w.find("1")
            last = w.find("\n", start)
            dict_["text"] = w[(start):last].replace("1. ", "").replace("1) ", "").encode("utf-8")
            word.append(dict_)
            
        elif "1." in w:
            start = w.find("1")
            last = w.find("\n", start)
            dict_["text"] = w[(start):last].replace("1. ", "").replace("1) ", "").encode("utf-8")
            word.append(dict_)
            
        elif "1." or "1) " not in w:
            if "\n" in w:
                last = w.find("\n")
                dict_["text"] = w[0:last].encode("utf-8")
                word.append(dict_)
                
            else:
                dict_["text"] = w.encode("utf-8")
                word.append(dict_)
                pass
        dict_["word_id_id"] = index   

with open('formatted-words/mysite_translation-with-index.json', 'w') as outfile:
	json.dump(word, outfile, indent = 4, ensure_ascii=False, sort_keys=False)