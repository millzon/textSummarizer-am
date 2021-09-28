# Amharic text summarizer

Generate [Amharic](https://en.wikipedia.org/wiki/Amharic) text summarizer using python


Algorithm 1: Extraction
1. Extract all the sentences from text.
2. Extract all the words from text.
3. Assign a score to each word.
4. Assign a score to each sentence.
5. Put the sentences with the highest score together in chronological order to produce the summary.

Algorithm 2: Cosine Similarity
1. TF-IDF weights to each individual word in a sentence
2. Generate cosine-similarity of each TF-IDF sentence pair matrix
3. Average the weights of each vector
4. Vectors with highest average summarize the text
words with higher weights (more unique) have more importance

Algorithm 3: word cloud based on: https://github.com/millzon/wordcloud-am

Algorithm 4: Abstract
- TODO

Intallation 

>pip install -r requirements.txt

>python main.py


Reference links: <br/>
- https://towardsdatascience.com/understand-text-summarization-and-create-your-own-summarizer-in-python-b26a9f09fc70
- https://github.com/icoxfog417/awesome-text-summarization#motivation
- https://blog.floydhub.com/gentle-introduction-to-text-summarization-in-machine-learning/
- https://github.com/AustinKrause/nyt-article-summarizer
- https://www.machinelearningplus.com/nlp/cosine-similarity/

