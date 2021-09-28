# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 14:39:35 2018

@author: milli

script to generate a wordcloud a free ebook
"""
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)
import pdfParser  as pp
import matplotlib.pyplot as plt
import matplotlib
import numpy
from wordcloud import WordCloud
import matplotlib.font_manager as font_manager
from PIL import Image
#plt.figure(figsize=(15,10))


def generate_wordcloud(text, stop_words,file_name):
    #removing stop words
    filtered_text_list = [val for val in text if val not in stop_words]
    filtered_text = ' '.join(filtered_text_list)

    wordcloud = WordCloud(font_path='fonts/jiretsl.ttf',
                        relative_scaling = 1.0,
                        min_font_size=4,
                        background_color="white",
                        width=1024,
                        height=768,
                        scale=3,
                        font_step=1,
                        collocations=True,
                        mode='RGBA',
                        repeat=True,
                        colormap=matplotlib.colors.ListedColormap (numpy.random.rand (256,3)),

                        margin=1
                        ).generate(filtered_text)

    plt.imshow(wordcloud, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    font_path = 'fonts/Arista2.0.ttf'
    prop = font_manager.FontProperties(fname=font_path)
    plt.text(0.5, 3.0, 'dirzon.com', font_properties=prop, fontsize = 16, color='darkorange',ha='center')
    
    #plt.show()
    plt.savefig('out\\'+file_name,dpi=600)

def fill_watermark(path):
    im = Image.open(path).convert('RGBA')
    bg = Image.new(mode='RGBA', size=im.size, color=(255, 255, 255, 0))
    logo = Image.open('out/t_logo.png')  # .rotate(45) if you want, bg transparent
    bw, bh = im.size
    iw, ih = logo.size
    for j in range(bh // ih):
        for i in range(bw // iw):
            bg.paste(logo, (i * iw, j * ih))
    im.alpha_composite(bg)
    im.show()

if __name__ == "__main__": 
    #book can be from downloaded  path or from url
    book_url = 'https://www.dirzon.com/Zon/DldAsync?target=Achamyeleh%20Dessie%3Auutaye.pdf'
    pparser = pp.pdfPrser(book_url)
    generate_wordcloud(pparser.words, pparser.stop_words,'word_cloud.png')
    #fill_watermark('out/word_cloud.png')
    print('.')