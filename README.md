# NLP
Portfolio for Python coding work for NLP

## Overview_of_NLP

An Overiew of my personal understanding of NLP:

(https://github.com/chris-straschewski/NLP/blob/276fd85136d7f9150f187e3bab150e5bf4f7b375/Overview_of_NLP.pdf)

## Text Processing

This program takes in the excel document as input, does error checking to make sure everything is correct, then outputs the data from the document in a particular fashion.

The program is run in the command line by typing "python Main data\data.csv"

From my experience with this assignment, python is very good at text processing. It was easy to make the program check that everything was formatted and input correctly, and removing spaces and newlines from the file was quite simple as well.

Nearly everything in the assignment was new. I have had to do text processing in other languages, but not in python. I was pleasantly surprised by how simple it was. The only thing that was a mild review was reading from a file, as I have already had to write a python program to do that in a different class i'm taking this semester:

(https://github.com/chris-straschewski/NLP/blob/1f074d4a48fa4c3b89bf75a70ede2f5d576deb94/Main)

## Word Guessing Game

This program takes a large text file, tokenizes it, and processes its text in various ways, all ultimately so that the 50 most common nouns can be collected and used for a Word Guessing Game. In the game, users lose points with an incorrectly guessed letter and gain points with a correctly guessed letter, and the game ends when they run out of points or type '!'.

My experience in writing this program will be very helpful whenever I need to tokenize and process text in python:

(https://github.com/chris-straschewski/NLP/blob/afa293aec16705b6264047f897bf96723dde1672/WGG.py)

## WordNet

This program dives into some of the features of WordNet and SentiWordNet, such as exploring the relations of words and their probabilities of appearing together within a text.

Wordnet is clearly significant to real world NLP applications and the calculations that need to be done for them.

(https://github.com/chris-straschewski/NLP/blob/a05fb8c10436f98de757ede19286c8ad2f2b8711/WordNet.ipynb%20-%20Colaboratory.pdf)

## Ngrams

This program explores some of the capacilities of Ngrams and their ability to calculate probabilities of words and phrases appearing in a text- something that is quite useful in applications that involve text predicting, correction, etc. 

Also included is a word doc containing more information about Ngrams.

Ngrams Part 1:(https://github.com/chris-straschewski/NLP/blob/3c4813da932cec6a495e3e4cea74705bada81709/Ngrams.py)

Ngrams Part 2:(https://github.com/chris-straschewski/NLP/blob/4500e0b612d583a99790c953323ac6776889be3f/Ngrams2.py)

Ngrams Narrative:(https://github.com/chris-straschewski/NLP/blob/4500e0b612d583a99790c953323ac6776889be3f/Narrative_Ngrams.docx)

## Sentence Parsing

A brief assignment where I was to come up with a complex sentence, then do a few things with it:

Create a PSG tree

Perform a Dependency parse

Perform an SRL parse

All three of these analyzed the sentence in different ways and are all useful in their own ways
(https://github.com/chris-straschewski/NLP/blob/d48a8ef69411e9fd0b3e9cae5dad7c91186fb106/Sentence%20Parsing.pdf)

## WebCrawler

Program that starts with a specific URL, extracts other URLs from that starting point, extracts text from those URLs, and extracts information with the goal of eventually creating a knowledge bot for a chatbot to use.

Code: (https://github.com/chris-straschewski/NLP/blob/f86b974486c2268fe90b194add0a347b139dd12c/WC.py)
Report: (https://github.com/chris-straschewski/NLP/blob/38826439e5b4def8f2e32097d71f2dc4d26c8de3/WebCrawler.docx)

## ML Text Classification

A program that takes a database from kaggle containing movie reviews from IMDB, and if they are considered to be positive or negative reviews.

In the program we have performed text to data transformation using vectorizers, split the data into a training set and test set, and made predictions using Naive Bayes, Logistic Regression, and a Neural Network.

Code: (https://github.com/chris-straschewski/NLP/blob/25dacecf8b20263e86b75c82c1d2aad1f33d9e0c/ML%20Text%20Classification.pdf)

## ACL Paper Summary

A summary about a paper creating a new model for measuring the cultural representativeness of NLP datasets based on geographic location.

Paper: (https://github.com/chris-straschewski/NLP/blob/d7c481689372ac1fd5fc7152bc5da97b6aa39a86/ACL%20Paper%20Summary.docx)

## Basic Chatbot 

Rough attempt at a chatbot on Dialogflow. Has minimal knowledge about Shrek, including some opinions and facts about characters, the movies, and actors.




