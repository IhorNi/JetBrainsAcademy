from lxml import etree
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.tokenize import word_tokenize
import string

from sklearn.feature_extraction.text import TfidfVectorizer


class KeyTermExtractor:

    def __init__(self, file_path):
        """Initialization with text preprocessing"""

        self.root = etree.parse(file_path).getroot()
        self.news_dict = dict()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = stopwords.words('english')

        for news in self.root.iter():
            if news.get('name') == 'head':
                key = news.text
            if news.get('name') == 'text':
                self.news_dict[key] = self.text_preprocessing(news.text)

    def __str__(self):
        """Function to print news headings with preprocessed text"""
        response = []
        for news, text in self.news_freq.items():
            response.append(f'{news}:\n{text}')

        return '\n'.join(response)

    def text_preprocessing(self, text, top_n=5):
        """
        Function to create bag-of-words with frequencies from unprocessed text
        Preprocessing steps are:
            1. Tokenization
            2. Lemmatization
            3. Removing stopwords and punctuation
            4. Only nouns should be left
        """

        word_tokens = sorted(word_tokenize(text.lower()), reverse=True)
        words_lemmas = [self.lemmatizer.lemmatize(word) for word in word_tokens]
        words_processed = [x for x in words_lemmas if x not in self.stop_words and x not in list(string.punctuation)]
        nouns = [x for x in words_processed if pos_tag([x])[0][1] == 'NN']

        return ' '.join(nouns)

    def extract_key_terms_to_string(self, top_n=5):
        """
        Function to get top_n key terms of a document based on TF-IDF scores
        Sorting, firstly, descending sorting by score, then descending sorting by strings (words)
        """

        text = list(self.news_dict.values())

        vectorizer = TfidfVectorizer()
        vectorizer.fit(text)

        for key, item in self.news_dict.items():
            vector = vectorizer.transform([item])
            feature_array = np.array(vectorizer.get_feature_names())
            response_dict = {feature_array[i]: vector.toarray()[0][i] for i in range(len(feature_array))}
            response_dict = sorted(response_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
            response_dict = {response_dict[i][0]: response_dict[i][1] for i in range(len(response_dict))}

            key_terms = list(response_dict.keys())[:top_n]
            print(f'{key}:\n{" ".join(sorted(key_terms))}')


KTE = KeyTermExtractor('news.xml')
KTE.extract_key_terms_to_string()

