#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import requests
import json
import collections

word = []
len_ = []

for i in range(0, 1168, 50):
	url = "https://sozdik.kz/suggest/kk/ru/%D0%B3/2/" + str(i) + "/50"
	req = requests.get(url).json()["suggests"]
	suggests_len = len(req)

	for j in range(0, suggests_len):
		r = req[j]
		if (" " not in 	r and "-" not in r):
			print r
			url = "https://sozdik.kz/translate/kk/ru/" + r + "/"
			tr = requests.get(url).json()["translation"]
			soup = BeautifulSoup(tr, "html5lib")
			letters = soup.get_text().encode("utf-8")

			dict_ = collections.OrderedDict()
			dict_["word"] = r.encode("utf-8")
			dict_["len"] = len(r)
			dict_["translation"] = letters

			word.append(dict_)


with open('letter-г.json', 'w') as outfile:
	json.dump(word, outfile, indent = 4, ensure_ascii=False, sort_keys=False)