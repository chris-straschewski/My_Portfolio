# Chris Straschewski
# CMS180014
# CS 4395.001

import pickle

# Program 2:

# Read in your pickled dictionaries

# English
unigram_english_dict = pickle.load(open('unigram_english_dict.p', 'rb'))
bigram_english_dict = pickle.load(open('bigram_english_dict.p', 'rb'))

# French
unigram_french_dict = pickle.load(open('unigram_french_dict.p', 'rb'))
bigram_french_dict = pickle.load(open('bigram_french_dict.p', 'rb'))

# Italian
unigram_italian_dict = pickle.load(open('unigram_italian_dict.p', 'rb'))
bigram_italian_dict = pickle.load(open('bigram_italian_dict.p', 'rb'))


# For each line in the test file, calculate a probability for each language (see note below) and
# write the language with the highest probability to a file.

import nltk
from nltk import word_tokenize
from nltk.util import ngrams

# total vocabulary size
v = len(unigram_english_dict) + len(unigram_french_dict) + len(unigram_italian_dict)

# open output file
file = open('data/wordLangId.out', 'w')

line_num = 1  # line number counter

# We must first read in the test file
with open('data/LangId.test', encoding="utf8") as f:  # open file that was set as parameter
    for line in f:  # go line by line

        # Initialize variables needed for probability calculation
        b1 = 0
        u1 = 0
        b2 = 0
        u2 = 0
        b3 = 0
        u3 = 0

        line = line.replace('\n', '')  # remove newlines

        tokens_test = word_tokenize(line)  # tokenize each line

        unigrams_test = tokens_test  # get unigram list for line
        bigrams_test = list(ngrams(tokens_test, 2))  # get bigram test for line

        for bigram in bigrams_test:  # iterate through bigrams in test data
            if bigram in bigram_english_dict:  # if bigram matches a bigram from a particular dictionary
                b1 += (bigram_english_dict[bigram])  # increment count of that bigram
                u1 += (unigram_english_dict[bigram[0]])  # and the first unigram in that particular bigram
            if bigram in bigram_french_dict:
                b2 += (bigram_french_dict[bigram])
                u2 += (unigram_french_dict[bigram[0]])
            if bigram in bigram_italian_dict:
                b3 += (bigram_italian_dict[bigram])
                u3 += (unigram_italian_dict[bigram[0]])

        english_probability = (b1 + 1) / (u1 + v)  # calculate probability of all three
        french_probability = (b2 + 1) / (u2 + v)
        italian_probability = (b3 + 1) / (u3 + v)

        if english_probability > french_probability:  # find largest probability
            if english_probability > italian_probability:
                file.write(str(line_num))  # print line number
                file.write(" English\n")  # print largest probability
            else:
                file.write(str(line_num))
                file.write(" Italian\n")
        else:
            if french_probability > italian_probability:
                file.write(str(line_num))
                file.write(" French\n")
            else:
                file.write(str(line_num))
                file.write(" Italian\n")

        line_num += 1  # increment line number

file.close()  # close output file


# Compute and output your accuracy as the percentage of correctly classified instances in the
# test set. The file LangId.sol holds the correct classifications.
file1 = open('data/wordLangId.out', 'r')
file2 = open('data/langId.sol', 'r')

# read both files line by line
file1_lines = file1.readlines()
file2_lines = file2.readlines()

# increment counters for correct lines, overal lines, and a list of error lines
n = 0
counter = 0
errors = []

# loop that ierates through both lists of file content and compares them
for i in range(len(file1_lines)):
    if file1_lines[i] == file2_lines[i]:
        n += 1  # correct line
    else:
        errors.append(i)  # error line found
    counter += 1  # count lines

# print accuracy
accuracy = n / counter
print("\nAccuracy:", accuracy * 100, "%")

# print error lines
print("\nlines with Errors:", errors)

# close both files
file1.close()
file2.close()







