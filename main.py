import fasttext
import os
from pathlib import Path

from numpy import cos
import pdfParser as pp
import extraction_summary
import cosine_similarity
import wordcloud_am

output_path = os.path.dirname(Path(__file__)) + '/out/'

def detect_language(text):
    model = fasttext.load_model(os.path.dirname(Path(__file__)) + '/fastText/lid.176.ftz')
    return model.predict(text, k=1)[0][0][-2:]

def save_text_file(file_name, text):
    with open(output_path + file_name, "w+",encoding="utf-8") as text_file:
        text_file.write(text)


if __name__ == "__main__":    

#read pdf
#detect language, if 'am' Continue
#make wordclouds, save image 
#make extraction summary, save text
#make cosine summary, save text
#make abstract summary, save text
#update db and continue
    logf = open("out/log.log", "a+")
    
    book_url = 'https://amnewsupdate.files.wordpress.com/2010/09/asteway.pdf'
    pparser = pp.pdfPrser(book_url)
    lang = detect_language(pparser.clean_text)
    if  lang == 'am':
        print('woriking...')
        #wordclouds
        print('word cloud...')
        wordcloud_am.generate_wordcloud(pparser.words, pparser.stop_words, 'word_cloud.png')
        #extraction
        print('extraction summary...')
        hyper_param = 1.5
        ext_summary = extraction_summary._get_summary(pparser,hyper_param)
        save_text_file('extraction_summary.txt',ext_summary)        
        #cosine summary
        print('cosine summary...')
        cos_summary = cosine_similarity.build_summary(pparser.sentences,pparser.stop_words)
        save_text_file('cosine_summary.txt',cos_summary)
        #abstract summary
        #TODO
    else:
        logf.write('language not supported: {0}: {1}\n '.format(book_url, lang))

    print('The End')