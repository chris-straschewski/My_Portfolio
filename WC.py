# Chris Straschewski
# CMS180014
# CS 4395.001

# Web Crawler

## Build a web crawler function that starts with a URL representing a topic
# and outputs a list of at least 15 relevant URLs. The URLs can be pages within
# the original domain but should have a few outside the original domain.

# First we need a starter URL
starting_url = "https://en.wikipedia.org/wiki/Shrek"

# Import soup and requests
from bs4 import BeautifulSoup
import requests

# Function that will loop through and save urls from the website
def url_looper(url):

    # get requests from starting url
    req = requests.get(url)

    # put the requests into text
    data = req.text

    # create a soup object with this text
    soup = BeautifulSoup(data, features="html.parser")

    # initialize counter
    counter = 0

    # write urls to a file to be read after
    with open('urls.txt', 'w') as f:
        for link in soup.find_all('a'):
            #print(link('href'))
            f.write(str(link.get('href')) + '\n\n')
            if counter > 20:
                break
            counter += 1

    #print("end of crawler")

url_looper(starting_url)

# Function that will loop through urls again but narrow down what gets saved
def url_looper2(url):

    req = requests.get(url)

    data = req.text

    soup = BeautifulSoup(data, features="html.parser")

    counter = 0

    with open('urls2.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            if 'Shrek' in link_str or 'shrek' in link_str:
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str:
                    if 'wikipedia' in link_str:
                        if 'en.wikipedia' in link_str and counter < 15:
                            f.write(link_str + '\n')
                            counter += 1
                    else:
                        if 'https://www.the-numbers.com/movie/Shrek' not in link_str and \
                                'https://web.archive.org' not in link_str and \
                                'telegraph.co' not in link_str and \
                                'nytimes' not in link_str and \
                                'yahoo' not in link_str and \
                                'digitalmediafx' not in link_str and \
                                'nicolas-cage' not in link_str and \
                                'jimhillmedia' not in link_str and \
                                counter < 15:

                            f.write(link_str + '\n')
                            counter += 1


    #print("end of crawler")

url_looper2(starting_url)

# Good links
# 1 https://commons.wikimedia.org/wiki/Category:Shrek_(2001_film)
# 2 https://en.wikiquote.org/wiki/Shrek
# 3 https://variety.com/2001/film/awards/shrek-3-1200468574/
# 4 https://variety.com/2001/scene/vpage/shrek-shleps-in-1117797904/
# 5 https://ew.com/article/2001/05/29/shrek-anti-disney-fairy-tale/
# 6 https://www.vulture.com/2020/12/national-film-registry-2020-dark-knight-grease-and-shrek.html
# 7 http://culture.com/articles/487/shrek-interview-with-mike-myers.phtml
# 8 http://cinema.com/articles/462/shrek-production-notes.phtml
# 9 https://www.indiewire.com/2010/04/dreamworks-tell-all-exposes-katzenberg-shrek-bail-out-238761/
# 10 http://shardlowart.blogspot.com/2010/05/shreks-house-early-concepts.html
# 11 http://culture.com/articles/463/shrek-production-information.phtml
# 12 https://usatoday30.usatoday.com/life/enter/movies/2001-05-18-shrek-more-characters.htm
# 13 https://www.cnn.com/2015/08/06/entertainment/chris-farley-shrek-voice-feat/
# 14 https://www.cbr.com/movie-legends-revealed-myers-minor-change-cost-shrek-4m/
# 15 https://www.thefreelibrary.com/Shrek's+appeal%3B+WHY+MYERS'+OGRE+JUST+HAD+TO+HAVE+SCOTS+ACCENT.-a0117830257


# Look at URLs that got saved
#with open('urls2.txt', 'r') as f:
    #urls2 = f.read().splitlines()
    #print('\nSaved URLs:')
#for i in urls2:
    #print(i)


## Write a function to loop through your URLs and scrape all text off each page.
## Store each page’s text in its own file.

# function to determine if an element is visible
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

import urllib.request
from urllib.request import urlopen, Request
import re

# function that gets text from the 15 chosen urls
def url_text(url):

    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features="html.parser")
    data = soup.findAll(text=True)
    result = filter(visible, data)
    temp_list = list(result)  # list from filter
    temp_str = ' '.join(temp_list)
    return temp_str

# run above function with our text file full of 15 relevant urls
# and put output into 15 text files
counter = 1

with open('urls2.txt', 'r') as f:
    urls = f.read().splitlines()
for i in urls:
    with open('url_text_' + str(counter) + '.txt', 'w', encoding="utf-8") as f:
        f.write(url_text(i))
        counter += 1

## Write a function to clean up the text from each file. You might need to delete newlines
## and tabs first. Extract sentences with NLTK’s sentence tokenizer. Write the sentences for
## each file to a new file. That is, if you have 15 files in, you have 15 files out.
import nltk
from nltk import sent_tokenize


def clean_text(filename, counter):

    # open passed file for text processing
    with open(filename, 'r', encoding="utf-8") as f:
        # read raw text and store it into a variable
        raw_text = f.read()

    # remove tabs and newlines
    raw_text = raw_text.replace('\n', ' ')
    raw_text = raw_text.replace('\t', ' ')

    # encoding the text to ASCII format
    text = raw_text.encode(encoding="ascii", errors="ignore")
    # decoding the text
    text = text.decode()
    # remove semicolons
    text = text.replace(';', ' ')
    # remove various other symbols
    text = text.replace('_', ' ')
    text = text.replace('|', ' ')
    text = text.replace('/', ' ')
    text = text.replace('<', ' ')
    text = text.replace('>', ' ')
    text = text.replace('\\', ' ')
    text = text.replace('/', ' ')
    text = text.replace('@', ' ')
    # cleaning the text to remove extra whitespace
    text = " ".join([word for word in text.split()])

    # lowercase all text
    text = text.lower()

    # done with text cleaning
    sentences = sent_tokenize(text)

    # create file for output
    with open('url_sentences_'+str(counter)+'.txt', 'w', encoding="utf-8") as f:
        # for loop to iterate through sentences and print them into file
        for sentence in sentences:
            f.write(sentence)

# For loop to send all 15 files into text cleaner and get the 15 sentence files
for i in range(1, 16):
    clean_text('url_text_'+str(i)+'.txt', i)

## Write a function to extract at least 25 important terms from the pages using an
## importance measure such as term frequency, or tf-idf. First, it’s a good idea to
## lowercase everything, remove stopwords and punctuation. Print the top 25-40 terms
from nltk.corpus import stopwords
def important_terms():

    # we will need a dict that counts word frequency
    word_frequency_dict = {}

    # open all 15 files one by one
    for i in range(1,16):
        with open('url_sentences_'+str(i)+'.txt', 'r', encoding="utf-8") as f:
            text = f.read()
            # tokenize text
            tokens = nltk.word_tokenize(text)

            tokens = [t for t in tokens if t.isalpha() and  # only alpha, remove punctuation
                      t not in stopwords.words('english')]  # remove stopwords

            for token in tokens:
                if token in word_frequency_dict:
                    word_frequency_dict[token] += 1
                else:
                    word_frequency_dict[token] = 1

    # sort the dict by count and print the 40 most common words and their counts
    sorted_word_freq_dict = dict(sorted(word_frequency_dict.items(), key=lambda x: x[1], reverse=True))
    important_words = dict(list(sorted_word_freq_dict.items())[0: 40])

    print("\n40 Most Common Words:", important_words)

    # Removing some unimportant words
    del important_words['end']
    del important_words['plus']
    del important_words['ad']
    del important_words['tv']
    del important_words['video']
    del important_words['tag']
    del important_words['account']
    del important_words['print']
    del important_words['subscribe']
    del important_words['zone']
    del important_words['menu']
    del important_words['get']
    del important_words['news']
    del important_words['content']
    del important_words['privacy']

    print("\nMost Common Words:", important_words)

    return important_words

    # from here I'll manually select the 10 most important terms in no particular order
    # character (shrek, donkey, fiona, farquaad)
    # film (movie)
    # myers
    # awards
    # animated
    # like
    # see
    # variety
    # icon

important_terms()


## Build a knowledge base
# Dict with sentences straight from the files +
# Dict with our most important terms
# ^ Both would be useful for a chatbot, these could be combined later

# Dict with sentences from the files
sent_dict = {}
for i in range(1,16):
    with open('url_sentences_'+str(i)+'.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        sentences = sent_tokenize(text)
        for sentence in sentences:
            if sentence in sent_dict:
                sent_dict[sentence] += 1
            else:
                sent_dict[sentence] = 1

print(sent_dict)

# Dict with best words was already made earlier, we will now pickle both dicts
import pickle

important_words = important_terms()

pickle.dump(sent_dict, open('sent_dict.p', 'wb'))
pickle.dump(important_words, open('important_dict.p', 'wb'))

sent_dict = pickle.load(open('sent_dict.p', 'rb'))
print('\n', sent_dict)

important_dict = pickle.load(open('important_dict.p', 'rb'))
print('\n', important_dict)