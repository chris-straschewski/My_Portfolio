# Chris Straschewski
# CMS180014
# CS 4395.001

import random  # library to choose random word from list of words
import sys  # to use sys.arg
import os  # to read file
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from random import seed
from random import randint


def process_text():

    fp = sys.argv[1]
    with open(os.path.join(os.getcwd(), fp), 'r') as f:
        lines = f.read()  # Read the input file as raw text
        f.close()  # Close file

        tokens = nltk.word_tokenize(lines)  # Tokenize raw text
        print("\nLexical diversity: %.2f" % (len(set(tokens)) / len(
            tokens)))  # Calculate the lexical diversity of the tokenized text and output it, formatted to 2 decimal places

        # text processing
        tokens = [t for t in tokens if t.isalpha() and  # only alpha, remove punctuation
                  t.lower and  # lowercase all text
                  t not in stopwords.words('english') and  # remove stopwords
                  len(t) > 5]  # word must be longer than 5 letters

        # lemmatize the tokens and use set() to make a list of unique lemmas
        wnl = WordNetLemmatizer()
        lemmas = [wnl.lemmatize(t) for t in tokens]  # lemmas
        unique_lemmas = list(set(lemmas))  # unique lemmas

        # POS tagging, print first 20
        tags = nltk.pos_tag(tokens)
        first_20_tags = tags[0:20]
        print("\nFirst 20 Tags:", first_20_tags)

        # create a list of only those lemmas that are nouns
        noun_tags = []
        for token, pos in tags:
            if pos == "NN":
                noun_tags.append(token)

        # print the number of tokens (from step a) and the number of nouns (step d)
        print("\nNumber of tokens after processing:", len(tokens))
        print("\nNumber of nouns:", len(noun_tags))

        return tokens, noun_tags # return tokens and nouns


def guessing_game(common):

    # give the user 5 points to start with; the game ends when their total score is negative, or
    # they guess ‘!’ as a letter
    points = 5

    print("\nLet's play a word guessing game!")

    counter = 1

    while points > 0:

        # pick random word
        seed()
        random_num = random.randint(0, 49)
        chosen_word = common[random_num]

        counter += 1
        guesses = ''

        while counter > 0:

            chances = 0

            for letter in chosen_word: # iterate through letters
                if letter in guesses:
                    print(letter, end=" ") # correct letter
                else:
                    print("_", end=" ") # underscore
                    chances += 1 # decrement points

            if chances == 0:

                print("\nYou solved it!\n")
                print("Current score:", points)

                print("\nGuess another word")
                counter -= 1
                break

            print()
            guess = input("Guess a letter:") # have user guess a letter
            if guess == '!':
                exit()

            guesses += guess

            if guess not in chosen_word:

                points -= 1
                print("Sorry, guess again. Score is", points) # wrong guess

                if points == 0:
                    print("You lose! haha!") # loser, game over
                    exit()

            else:
                points += 1
                print("Right! Score is", points) # correct guess




# main function
def main():

    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
    else:
        tokens, nouns = process_text()

    # Make dict of {noun:count of noun in tokens} items from the nouns and tokens lists;
    pos_dict = {}
    for noun in nouns:
        if noun in pos_dict:
            pos_dict[noun] += 1
        else:
            pos_dict[noun] = 1

    # sort the dict by count and print the 50 most common words and their counts
    sorted_pos_dict = dict(sorted(pos_dict.items(), key=lambda x: x[1], reverse=True))
    first_50_nouns = dict(list(sorted_pos_dict.items())[0: 50])
    print("\n50 Most Common Words:", first_50_nouns)

    # Save these words to a list
    common_list = list(first_50_nouns.keys())

    guessing_game(common_list)


main()
