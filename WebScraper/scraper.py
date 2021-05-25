import requests
import os
import string
from bs4 import BeautifulSoup

translator = str.maketrans('', '', string.punctuation)


class NatureArticleParser():

    def __init__(self, topic_='News', page_num_=1):
        self.topic = topic_
        self.page_num = page_num_
        self.url_ = 'https://www.nature.com/nature/articles'

    @staticmethod
    def tag_containing_article_title(tag):
        return tag.name == "h1" and ("article" in tag["class"][0] and "title" in tag["class"][0])

    @staticmethod
    def tag_containing_article_body(tag):
        return tag.name == "div" and ("article" in tag.get("class", [""])[0] and "body" in tag.get("class", [""])[0])

    def filter_articles_by_topic(self, articles_):
        """Function to filter all articles from page by topic"""

        return [article for article in articles_
                if article.find('span', {'class': 'c-meta__type'}).text == self.topic]

    def scrap_pages(self):
        """Wrapper to iterate over given amount of pages on self.url_"""

        for i in range(1, self.page_num + 1):
            self.save_nature_news(i)

    def save_nature_news(self, page_number=1):
        """Function to save certain topic articles from 'https://www.nature.com/nature/articles' at specific page"""

        folder = f'Page_{page_number}'
        try:
            os.makedirs(folder)
        except FileExistsError:
            pass
        try:
            params = {
                'searchType': 'journalSearch',
                'sort': 'PubDate',
                'page': page_number
            }
            r = requests.get(self.url_, params=params)
            r.raise_for_status()
            soup = BeautifulSoup(r.content, 'html.parser')
            articles = soup.find_all('article')
            articles = self.filter_articles_by_topic(articles)

            for article in articles:

                try:
                    topic_url = article.find('a', {'data-track-action': 'view article'}).get('href')
                    topic_url = f'https://www.nature.com{topic_url}'

                    topic_header = article.find(self.tag_containing_article_title).text
                    topic_header = topic_header.text.translate(translator).strip()
                    topic_header = topic_header.replace(' ', '_')

                    topic_r = requests.get(topic_url)
                    topic_soup = BeautifulSoup(topic_r.content, 'html.parser')
                    #  body = topic_soup.find('div', {'class': 'article-item__body'})\
                    #  or topic_soup.find('div', {'class': 'article__body'})
                    body = topic_soup.find(self.tag_containing_article_body)
                    body = body.text.strip()
                    with open(f'{folder}/{topic_header}.txt', 'w', encoding='utf-8') as article_file:
                        article_file.write(body)
                except requests.HTTPError:
                    print(f'Problems with {topic_url}')

        except requests.HTTPError:
            print(f'Web scrapping failed at page {page_number}')


page_num = int(input())
topic = input()
nature_reader = NatureArticleParser(topic, page_num)
nature_reader.scrap_pages()
print('Saved all articles.')
