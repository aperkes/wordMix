import re
import itertools
import sys
import random

#word_file = './3-letter-words.txt'
#word_file = './3-common-words.txt'
word_file = './3-basic-words.txt'
#n_words = int(sys.argv[1])

word_list = []
with open(word_file,'r') as f:
    for line in f:
        if '#' not in line and len(line) > 2:
            word_list.append(line.strip())

#print(word_list)
#random.shuffle(word_list)
#for subset in itertools.combinations_with_replacement(word_list,3):

def join_lists(work_list):
    combo_list = []
    sub_words = [w[:-1] for w in word_list]
    sub_dict = dict(zip(sub_words,[1] * len(sub_words)))
    #for subset in itertools.combinations(word_list,2):
    for w1 in word_list:
        try: 
            sub_dict[w1[:-1]]
        except:
            continue
        for w2 in work_list:
            #if w1 in w2: ## exclude repeats
            #    continue
            potential = True
            subset = [w1,w2]
            flat_string = w1+w2 
            shifted_string = flat_string[1:]
            split_shifted = re.findall('...?',shifted_string)
            for w in split_shifted[:-1]:
                if w not in word_list:
                    potential = False
                    break
            if potential:
                #print(subset)
                combo_list.append(''.join(subset))

    return combo_list

combo_list = join_lists(word_list)
print(combo_list)
if len(combo_list) > 1000:
    combo_list = random.sample(combo_list,1000)

double_combo = join_lists(combo_list)
print(double_combo)
if len(double_combo) > 1000:
    double_combo = random.sample(double_combo,1000)

triple_combo = join_lists(double_combo)
if len(triple_combo) > 1000:
    triple_combo = random.sample(triple_combo,1000)
print(triple_combo)

quad_combo = join_lists(triple_combo)
print(quad_combo)
if len(quad_combo) > 1000:
    quad_combo = random.sample(quad_combo,1000)

five_combo = join_lists(quad_combo)
five_combo = random.sample(five_combo,1000)
#print(quad_combo)

for q in quad_combo[:100]:
    q_split = re.findall('...?',q)
    q_shift = re.findall('...?',q[1:])
    print(q_split)
    print(q_shift)
    print('')

for q in five_combo[:100]:
    q_split = re.findall('...?',q)
    q_shift = re.findall('...?',q[1:])
    print(q_split)
    print(q_shift)
    print('')
