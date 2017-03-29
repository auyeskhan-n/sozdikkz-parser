#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import requests
import json

word = []
len_ = []

for i in range(0, 50, 50):
	for j in range(0, 10):
		url = "https://sozdik.kz/suggest/kk/ru/%D0%90/2/" + str(i) + "/50"
		r = requests.get(url).json()["suggests"][j]
		if (" " not in 	r and "-" not in r):
			print r
			url = "https://sozdik.kz/translate/kk/ru/" + r + "/"
			tr = requests.get(url).json()["translation"]
			soup = BeautifulSoup(tr, "html5lib")
			letters = soup.get_text().encode("utf-8")
			print letters

			dict_ = {"word": r.encode("utf-8"), "translation": letters, "len": len(r)}
			word.append(dict_)
			#len_.append(len(r))


with open('data.json', 'w') as outfile:
	json.dump(word, outfile, indent = 4, ensure_ascii=False, sort_keys=False)


'''
url = "https://sozdik.kz/suggest/kk/ru/%D0%90/2/0/1"
print requests.get(url).json()["suggests"][1]
'''

'''
req = url.json()['translation'].encode("utf-8")
#print req

with open('data.json', 'w') as outfile:
    json.dump(r.text.encode("utf-8"), outfile, indent = 4, ensure_ascii=False)


soup = BeautifulSoup(req, "html5lib")
letters = soup.get_text()

print letters

with open('data.json', 'w') as outfile:
    json.dump(letters, outfile, indent = 4, ensure_ascii=False)

'''
