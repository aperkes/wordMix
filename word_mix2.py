import random
import re

word_list = []

letter_dict0 = {}
letter_dict1 = {}
word_dict0 = {}
word_dict1 = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for a in alphabet:
    letter_dict0[a] = []
    letter_dict1[a] = []

with open('./4-basic-words.txt') as f:
    for l in f:
        if '#' in l:
            continue
        else:
            word = l.strip()
            word_list.append(word.lower())
            #letter_dict[word[0]] = [] 

## First, need two dictionaries
## One which links words to the letters that need to follow them
## A second which links the letters to the words that start with them 
for word in word_list:
    
    word_shift = word[1:]
    first_letter = word[0]
    for a in alphabet:
        if word_shift + a in word_list:
            letter_dict0[first_letter].append(word)
            if word not in word_dict0.keys():
                word_dict0[word] = []
            word_dict0[word].append(a)

## We then do this a second time, because I don't want dead ends
#print(word_dict0.keys())
for word in word_dict0.keys():
    word_shift = word[1:]
    first_letter = word[0]
    for a in alphabet:
        if word_shift + a in word_dict0.keys():
            letter_dict1[first_letter].append(word)
            if word not in word_dict1.keys():
                word_dict1[word] = []
            word_dict1[word].append(a)

#print(letter_dict1)
#print(word_dict1)

letter_list1 = list(letter_dict1.keys())
word_list1 = list(word_dict1.keys())

## Now we just can walk through at random to generate arbitrary numbers of strings. 

length = 5
for i in range(100):
    one_string = []
    word = random.choice(word_list1)
    one_string.append(word)
    for n in range(length - 1):
        next_letter = random.choice(word_dict1[word])
        next_word = random.choice(letter_dict1[next_letter])
        one_string.append(next_word)
        word = next_word
    flat_string = ''.join(one_string)
    shifted_string = flat_string[1:]
    split_shifted = re.findall('....?',shifted_string)

    print(one_string)
    print(split_shifted)
    print('')
