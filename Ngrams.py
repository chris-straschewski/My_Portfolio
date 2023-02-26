# Chris Straschewski
# CMS180014
# CS 4395.001

# In this homework you will create bigram and unigram dictionaries for English, French, and Italian
# using the provided training data where the key is the unigram or bigram text and the value is the
# count of that unigram or bigram in the data. Then for the test data, calculate probabilities for
# each language and compare against the true labels.


# Program 1: Build separate language models for 3 languages as follows.

# create a function with a filename as argument
def language_model(filename):

    # read in the text and remove newlines
    from nltk import word_tokenize
    with open(filename, encoding="utf8") as f:  # open file that was set as parameter
        raw_text = f.read()  # read raw text

    raw_text = raw_text.replace('\n', '')


    # tokenize the text
    import nltk
    from nltk import word_tokenize
    tokens = word_tokenize(raw_text)


    # use nltk to create a bigrams list
    # use nltk to create a unigrams list
    from nltk.util import ngrams


    # create birgrams list
    bigrams = list(ngrams(tokens, 2))


    # unigrams list will just be the tokens themselves
    unigrams = tokens


    # use the bigram list to create a bigram dictionary of bigrams and counts, [‘token1 token2’] ->
    # count
    bigram_dict = {bigram: bigrams.count(bigram) for bigram in set(bigrams)}


    # use the unigram list to create a unigram dictionary of unigrams and counts, [‘token’] ->
    # count
    unigram_dict = {token: unigrams.count(token) for token in set(unigrams)}


    # return the unigram dictionary and bigram dictionary from the function
    return unigram_dict, bigram_dict


def main():

    # Call the function 3 times for the 3 different files
    # Pickle the dictionaries

    import pickle

    # English
    unigram_english_dict, bigram_english_dict = language_model("data/Langid.train.English")
    pickle.dump(unigram_english_dict, open('unigram_english_dict.p', 'wb'))
    pickle.dump(bigram_english_dict, open('bigram_english_dict.p', 'wb'))


    # French
    unigram_french_dict, bigram_french_dict = language_model("data/Langid.train.French")
    pickle.dump(unigram_french_dict, open('unigram_french_dict.p', 'wb'))
    pickle.dump(bigram_french_dict, open('bigram_french_dict.p', 'wb'))


    # Italian
    unigram_italian_dict, bigram_italian_dict = language_model("data/Langid.train.Italian")
    pickle.dump(unigram_italian_dict, open('unigram_italian_dict.p', 'wb'))
    pickle.dump(bigram_italian_dict, open('bigram_italian_dict.p', 'wb'))

main()