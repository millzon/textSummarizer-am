# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 2021

"""

from tika import parser
import string
import re

import os.path

class pdfPrser:

    def get_stop_words():
        return  open(os.path.dirname(__file__) + '/data/stopwords.txt', encoding='utf-8').read().split()


    # init method or constructor 
    am_sent_endings = r'\?|\!|\።|\፡፡'#".|?|!|።"
    am_punctuation = '፠፡።፣፤፥፦፧፨“”‘’…‹‹››·•'
    am_numbers = '፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻፼'
    am_random = '�©\uf0c4\uf0d8\uf0a7\uf066\uf0d8' 
    stop_words = get_stop_words()

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.raw_text = None
        self.clean_text = None
        self.sentences = None
        self.words = None

        self.parse(pdf_path)


    #reading old pdf files with non-unicode fonts has been imposible 
    def parse(self, path):
        self.raw_text = parser.from_file(path)['content']
        #remove duplicated spaces and return
        #return " ".join(raw['content'].split())
        self.clean_text = self.clean_minimized(self.raw_text)
        self.sentences = self.extract_sentences(self.clean_text)
        #remove duplicates
        self.sentences = self.remove_duplicate_sentence(self.sentences)
        self.words = self.extract_words(self.clean_text)


    def extract_sentences(self, text=None):
        '''generates a list of sentences'''
        if text == None: text=self.raw_text
        sentences = re.split(self.am_sent_endings,text)
        return sentences
    
    def extract_words(self, text):
        '''generates a list of words'''    
        return text.split()

    def clean(self, text):
        # split into words by white space
        words = text.split()   
        to_clean = string.punctuation + self.am_numbers + self.am_random + string.ascii_letters + string.digits + self.am_punctuation    
        table = str.maketrans('', '', to_clean)
        stripped = [w.translate(table) for w in words]
        #remove empty strings from list
        clean_txt = list(filter(None, stripped))
        return clean_txt

    def clean_minimized(self, text):
        # split into words by white space
        words = text.split()   
        to_clean = string.punctuation + self.am_numbers + self.am_random + string.ascii_letters + string.digits + self.am_punctuation
        to_clean = re.sub(self.am_sent_endings,'',to_clean)
        table = str.maketrans('', '', to_clean)
        stripped = [w.translate(table) for w in words]
        #remove empty strings from list
        clean_txt = list(filter(None, stripped))
        return ' '.join(clean_txt)
    
    def remove_duplicate_sentence(self,sentences):
        duplicates = []
        cleaned = []
        for s in sentences:
            if s in cleaned:
                if s in duplicates:
                    continue
                else:
                    duplicates.append(s)
            else:
                cleaned.append(s)
        return cleaned

#Test
if __name__ == '__main__':
    pd_parser = pdfPrser('https://www.dirzon.com/Zon/DldAsync?target=telegram%3Amesethiru%20sigalathe.pdf')
    print(pd_parser.words)
