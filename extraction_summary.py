import os, sys
import re
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import pdfParser as pp


def _create_dictionary_table(words) -> dict:
    # Creating dictionary for the word frequency table
    frequency_table = dict()
    #words = text_string.split() 

    for wd in words:
        #wd = stem.stem(wd)
        #if wd in stop_words:
        #    continue
        if wd in frequency_table:
            frequency_table[wd] += 1
        else:
            frequency_table[wd] = 1

    return frequency_table

def _calculate_sentence_scores(sentences, frequency_table) -> dict:   

    #algorithm for scoring a sentence by its words
    sentence_weight = dict()

    for sentence in sentences:
        #sentence = ' '.join(sentence)
        #sentence_wordcount = (len(sentence.split()))
        sentence_wordcount_without_stop_words = 0
        words = sentence.split() 
        for word in words:
            if word in frequency_table:
                sentence_weight[sentence] = frequency_table[word]

        #sentence_weight[sentence] = sentence_weight[sentence]/len(words)


        
        # for word_weight in frequency_table:
        #     if word_weight in sentence      #.lower():
        #         sentence_wordcount_without_stop_words += 1
        #         if sentence[:7] in sentence_weight:
        #             sentence_weight[sentence[:7]] += frequency_table[word_weight]
        #         else:
        #             sentence_weight[sentence[:7]] = frequency_table[word_weight]

        # sentence_weight[sentence[:7]] = sentence_weight[sentence[:7]] / sentence_wordcount_without_stop_words       

    return sentence_weight

def _calculate_average_score(sentence_weight) -> int:
   
    #calculating the average score for the sentences
    sum_values = 0
    for entry in sentence_weight:
        sum_values += sentence_weight[entry]

    #getting sentence average value from source text
    average_score = (sum_values / len(sentence_weight))

    return average_score

def _get_article_summary(sentences, sentence_weight, threshold):
    sentence_counter = 0
    article_summary = ''

    for sentence in sentences:
        #sentence = ' '.join(sentence)
        if sentence in sentence_weight and sentence_weight[sentence] >= (threshold):
            article_summary += sentence + '።'
            sentence_counter += 1
    #remove duplicate phrase
    article_summary = re.sub(r'((\b\w+\b.{1,2}\w+\b)+).+\1', r'\1', article_summary, flags = re.I)

    return article_summary

def _get_summary(pparser, treshold_parameter=1.5):
    sentences = pparser.sentences

    #creating a dictionary for the word frequency table
    frequency_table = _create_dictionary_table(pparser.words)

    #tokenizing the sentences
        #we have sentences

    #algorithm for scoring a sentence by its words
    sentence_scores = _calculate_sentence_scores(sentences, frequency_table)    

    #getting the threshold
    threshold = _calculate_average_score(sentence_scores)

    #producing the summary
    return _get_article_summary(sentences, sentence_scores, treshold_parameter * threshold)


if __name__ == "__main__":
    book_url = ''
    pparser = pp.pdfPrser(book_url)
    article_summary = _get_summary(pparser)
    print(article_summary)