# JetBrainsAcademy NLP Track - Key Term Extraction

Extracting keywords can help you get to the text meaning. Also, It can help you with splitting texts into different categories. In this project, I learned how to extract relevant words from a collection of news stories. There are many different ways to do it, but I focused on frequencies, part-of-speech search, and TF-IDF methods. 

### Objectives

1. Read an XML-file containing stories and headlines.
2. Extract the headers and the text.
3. Tokenize each text.
4. Lemmatize each word in the story.
5. Get rid of punctuation, stopwords, and non-nouns with the help of NLTK.
6. Count the TF-IDF metric for each word in all stories.
7. Pick the five best scoring words.
8. Print each story's headline and the five most frequent words in descending order. Take a look at the sample output below. Display the titles and keywords in the same order they are presented in the file.

# JetBrainsAcademy Python Track - Web Calendar

These days, our lives are very busy and eventful. It's very hard to keep track of everything that happens around us. Let's create a web calendar that will store and manage all upcoming events. Use the Flask framework and create a REST API to save and manage events. The Flask framework allows you to start a web application from a single Python file.

This is a simple REST service with the Flask framework. It works with a database using the Flask-SQLAlchemy extension and create resources using the Flask-RESTful extension.

### Objectives

1. Endpont '/event': **GET** either all events or events between dates if any; **POST** new events with required name and date.
2. Endpont '/event/<int:event_id>': **GET** event by ID if any; **DELETE** event by ID if any.
3. Endpoint '/event/today': **GET** all events for today() if any. 

# JetBrainsAcademy NLP Track - RandomTextGenerator

A simple text generator using Markov chains that can predict the next word in a pseudo-sentence based on the previous words in the sequence and the data that is used to create a statistical model.

A Markov chain is a statistical model in which the probability of each event depends on the previous event. It can be described as a set of states and transitions between them. Each transition has a probability that is determined by some kind of statistical data. In this project, a state corresponds to a token, and each transition represents going from one word of a sentence to another. The probability of transitions is calculated from the bigrams we collected in the previous stage. The basic idea of this project is that from a dictionary we can create a model that will consider all the possible transitions from one word to another and choose the most probable one based on the previous word.

# JetBrainsAcademy NLP Track - WebScraper
We now have a good deal of knowledge and experience, so let's put it all together and create your first real web scraper. Most of the time, the reason why people create parse-and-scrape programs is to automate the routine tasks of retrieving large data from a website. For example, every machine learning task requires some train data. Let's imagine you're doing research based on the recent science news. For that research, you'll need to have the most recent articles with the type "News" that are posted on the Nature journal website. Each article should be saved to a separate .txt file named after the article's title.

### Objectives - 1
1. Create a program that takes the https://www.nature.com/nature/articles URL and then goes over the page source code searching for articles.
2. Detect the article type and the link to view the article tags and their attributes.
3. Save the contents of each article of the type "News" to a separate file named *%article_title%.txt*. Replace the whitespaces with underscores and remove punctuation marks in the filename (str.maketrans and string.punctuation will be useful for this). Also, strip all trailing whitespaces in the article body and title.
4. (Optional) You may output some result message once the saving is done, but it is not required.

We need to inspect each article to find the tags that represent the article's contents. If you take a closer look at the source code, you will see that every article is enclosed in a pair of \<article> tags. Then, each article type is hidden inside a <span> tag containing the data-test attribute with the article.type value. Also, every article includes a link to the article's contents, which is placed inside the <a> tag with the data-track-action="view article" attribute. Once the article page is loaded, save its body wrapped in the \<div> tag (look for "body" in the class attribute).

  
### Objectives - 2
1. Improve your code so that the function can take two parameters from the user input: the number of pages (an integer) and the type of articles (a string). The integer with the number of pages specifies the number of pages on which the program should look for the articles.
2. Go back to the https://www.nature.com/nature/articles website and find out how to navigate between the pages with the requests module changing the URL.
3. Create a directory named Page_N (where N is the page number) for each page in the desired category, and put all the articles that are found on the page with the matched type to this directory.
4. Save the articles to separate *.txt files. Keep the same processing of the titles for the filenames as in the previous stage. You can give users some feedback on completion, but it is not required.
If there's no articles on the page, your program should still create a folder, but in this case the folder would be empty.


# JetBrainsAcademy Python Track - Matrix Project
Python Track Projects
Here’s a project for devoted matrix enthusiasts: learn to perform a variety of operations on matrices including addition, multiplication, finding the determinant, and dealing with inverse matrices. If you are working on your tech or math major, this project is a good chance for you to learn matrices in action and not just in your notebook.
### Learning outcomes
Apart from learning a whole lot about matrices, you will become familiar with the Math library, recursion, and the many ways of using nested lists in practice.
This project is a part of the following track
### Demo
"demonstration.mp4" video shows all functionality of the project
