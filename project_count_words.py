# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:04:22 2021

@author: robert
"""
import sys
import PyPDF2
import re
import pattern
from pattern.text.en import singularize
import string
"""

pdfFileObj = open('Samplech7.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pdfData=''
for page in pdfReader.pages:
    pdfData += page.extractText()
# print(pdfData)

pattern = r"\(\d\s+('?\w+)"
results = re.findall("[a-zA-Z\-\.'/]+",pdfData)
print(results)

freq = {}
for piece in results:
    # only consider alphabetic characters within this piece
  word = ''.join(c for c in piece if c.isalpha())
  if word:                                # require at least one alphabetic character
    freq[word] = 1 + freq.get(word, 0)
print(freq)
"""

class WordAnalysis:
    def __init__(self):
        self.__toBeRemoved=[]
        self.__dictionary = dict()
        self.__wordlist = ''
        
    def __str__(self):
        s=''
        n=0
        for key, value in self.__dictionary.items():
            s+=('{:<14} {:<3}'.format( key, value))
            n += 1
            n = n%4
            if n == 0:
                s += '{}'.format('\n')
        return s
             
    def AddRemovedWords(self, word):
        self.__toBeRemoved.append(' '+word+' ')
#        print(self.__toBeRemoved)
        
    def DelRemovedWords(self, word):
        word = ' '+word+' '
        if word in self.__toBeRemoved:
            self.__toBeRemoved.remove(word)
#        print(self.__toBeRemoved)
            
    def ExtractWords(self, text):
        self.__wordlist=re.findall("[a-zA-Z\-\.'/]+", text)
        cleanText = ''        
        for i in range(len(text)):
            if text[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                cleanText += text[i].lower()
            else:
                cleanText += ' '
        for i in self.__toBeRemoved:
                cleanText = cleanText.replace(i," ")
                
        wordList=list(cleanText.split())
        singularWords = [singularize(plural) for plural in wordList]
        
        for word in singularWords:
            if len(word) != 1: 
                if word in self.__dictionary:
                    # If element exists in dict then increment its value else add it in dict
                    self.__dictionary[word] += 1
                else:
                    self.__dictionary[word] = 1

    def Show(self, freq):
        s=''
        dictOfWords = {key:value for key, value in self.__dictionary.items() if value > freq}
        
        for key, value in sorted(dictOfWords.items(), key=lambda x: x[1], reverse = True):
            s += ('{} {:^15} {} {} {}'.format( "word --", key,'-- frequency:', value, "\n"))
        print(s)
        
pdfFileObj = open('Samplech7.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfData=''
for page in pdfReader.pages:
    pdfData += page.extractText()
print(pdfData)

wordAnalysis = WordAnalysis()

wordAnalysis.AddRemovedWords("and")
wordAnalysis.AddRemovedWords("a")
wordAnalysis.AddRemovedWords("the")
wordAnalysis.AddRemovedWords("is")
# wordAnalysis.DelRemovedWords("a")

wordAnalysis.ExtractWords(pdfData)
wordAnalysis.Show(10)
print (wordAnalysis)


pdfFileObj.close() 