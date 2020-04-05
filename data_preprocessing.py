from nltk.stem import PorterStemmer
from gensim.parsing.preprocessing import STOPWORDS
from nltk.tokenize import word_tokenize
import pandas as pd
import re
import smart_open
import string
import sys
# -*- coding: utf-8 -*-
data=pd.read_csv(r'D:\20192\machine_learning\data\train.crash',header=None, error_bad_lines=False)
# INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐ"
# #INTAB = [ch.encode('utf8') for ch in unicode(INTAB, 'utf8')]

INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ"
INTAB = [ch.encode('utf8') for ch in unicode(INTAB, 'utf8')]
OUTTAB = "a" * 17 + "o" * 17 + "e" * 11 + "u" * 11 + "i" * 5 + "y" * 5 + "d" + \
         "A" * 17 + "O" * 17 + "E" * 11 + "U" * 11 + "I" * 5 + "Y" * 5 + "D"

r = re.compile("|".join(INTAB))
replaces_dict = dict(zip(INTAB, OUTTAB))


def no_accent_vietnamese(utf8_str):
    return r.sub(lambda m: replaces_dict[m.group(0)], utf8_str)
def combine_word(word):
    word=no_accent_vietnamese(word)
    if word.islower() == True:
        return word
    else:
        words = re.findall('[A-Z][a-z]*', word)
        res=''
        for w in words:
            w=chr(ord(w[0])+32)+w[1:]
            res+=w
            res+=' '
        return res
cnt=0
remove = ['(', ')', '"','?','!','.','❤️',':((','T^T']
all_docs=[]
for line in data[0]:
    if cnt%3!=1:
        cnt+=1
        continue
    cnt+=1
    words=word_tokenize(line)
    words=[combine_word(w) for w in words]
    words=[w for w in words if w not in remove]
    words=[w for w in words if w.isalpha()]
    all_docs.append(words)
with smart_open.smart_open('word2vec.txt', 'w') as f:
    for review in all_docs:
        for item in review:
            f.write("%s " % item)
        f.write("\n")







