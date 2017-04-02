#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

data = []

letters = ['а', 'ә', 'б', 'в', 'г', 'ғ', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'қ', 
            u'л', 'м', 'н', 'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ұ', 'ү', 'ф', 
            u'х', 'ц', 'ч', 'ш', 'ы', 'і', 'э', 'ю', 'я']
len_ = 0

for i in letters:
    uri = 'parsed-words/letter-' + i + '.json'
    with open(uri, 'r') as f:
        data = json.load(f)
        len_ += len(data)
        print len(data)
        
print len_
print len(letters)


# with open("formatted-words/data.json", 'r') as f:
#     data = json.load(f)
#     print len(data)