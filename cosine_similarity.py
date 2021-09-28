
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
import pdfParser as pp
from sklearn import feature_extraction
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances_argmin_min
import nltk
nltk.download('punkt')
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def find_similarities(sentences, stopwords):
    #tokenize sentences
    #sentences = sent_tokenize(text, language = 'en')
    #sentences = text.sentences
    #set stop words
    #stops = list(set(stopwords.words('english'))) + list(punctuation)
    
    #vectorize sentences and remove stop words
    vectorizer = TfidfVectorizer(stop_words = stopwords)
    #transform using TFIDF vectorizer
    trsfm=vectorizer.fit_transform(sentences)
    
    #creat df for input article
    text_df = pd.DataFrame(trsfm.toarray(),columns=vectorizer.get_feature_names(),index=sentences)
    
    #declare how many sentences to use in summary
    num_sentences = text_df.shape[0]
    num_summary_sentences = int(np.ceil(num_sentences**.5))
        
    #find cosine similarity for all sentence pairs
    similarities = cosine_similarity(trsfm, trsfm)
    
    #create list to hold avg cosine similarities for each sentence
    avgs = []
    for i in similarities:
        avgs.append(i.mean())
     
    #find index values of the sentences to be used for summary
    top_idx = np.argsort(avgs)[-num_summary_sentences:]
    
    return top_idx


def build_summary(sentences, stopwords):
    #find sentences to extract for summary
    sents_for_sum = find_similarities(sentences, stopwords)
    #sort the sentences
    sort = sorted(sents_for_sum)
    #display which sentences have been selected
    print('Number of selected sentences',len(sort))
    
    sent_list = sentences#sent_tokenize(text)
    #print number of sentences in full article
    print('Total number of sentences', len(sent_list))
    
    
    #extract the selected sentences from the original text
    sents = []
    for i in sort:
        sents.append(sent_list[i].replace('\n', '') + '።') 
    
    #join sentences together for final output
    summary = ' '.join(sents) 
    return summary

if __name__ == "__main__":
        book_url = 'https://www.dirzon.com/Zon/DldAsync?target=telegram%3Amesethiru%20sigalathe.pdf'
        pparser = pp.pdfPrser(book_url)
        article_summary = build_summary(pparser.sentences)
        print(article_summary)
