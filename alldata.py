import numpy as np
import pandas as pd
from googletrans import Translator
from os import listdir
import re
import time
import re

file_names=listdir("files")


translator = Translator()
# # translate a spanish text to arabic for instance
# translation = translator.translate("Hola Mundo", dest="ar")
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


def printlist(mlist):
    for line in mlist:
        print(line)
def FileProcessing(fname):
# Data Extraction
    f = open("files/"+fname, "r")
    text = f.readlines()
    result = []
    count = 0
    for line in text:
        if count % 2 == 0:
            result.append(line)
        count += 1

    istext = 1
    h1 = 0
    text = ''
    abst = ''
    for x in result:
        if h1:
            abst += x
            h1 = 0
        if x == '@highlight\n':
            istext = 0
            h1 = 1
        if istext:
            text += x

    # Abstract Translation
    list_sentences = abst.split('\n')
    cleaned_abst = []
    ur_abst = []
    for y in list_sentences:
        c_sen = re.sub(r'[^A-Za-z0-9@]+', ' ', y)
        cleaned_abst.append(c_sen)
        print('Translating : ',c_sen)
        t_txt = translator.translate(c_sen, dest='ur')
        print('Translated to : ',t_txt.text)
        ur_abst.append(t_txt.text)
        time.sleep(25)

    a_eng = ". ".join(cleaned_abst)
    a_urd = ". ".join(ur_abst)

    # Text Translation
    list_sentences = text.split('.')
    cleaned_sentences = []
    ur_sentences = []
    for y in list_sentences:
        c_sen = re.sub(r'[^A-Za-z0-9@]+', ' ', y)
        cleaned_sentences.append(c_sen)
        print('Translating : ',c_sen)
        t_txt = translator.translate(c_sen, dest='ur')
        print('Translated to : ',t_txt.text)
        ur_sentences.append(t_txt.text)
        time.sleep(25)

    t_eng = ". ".join(cleaned_sentences)
    t_urd = ". ".join(ur_sentences)

    # Saving into csv file
    data = [[a_eng,a_urd,t_eng,t_urd]]
    df = pd.DataFrame(data,
                   columns =["SummaryEng","SummaryUr","TextEng","TextUr"])
    df.to_csv(fname+".csv", index = False)

for f in file_names:
    FileProcessing(f)
