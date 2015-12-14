import nltk
from nltk.tokenize import word_tokenize
import poetry
import os.path
import re

here = os.path.dirname(os.path.realpath(__file__))
paradise = nltk.corpus.gutenberg.raw('milton-paradise.txt')
pastoral = open(here + '\\texts\pastoral-poems.txt').read()
poppy = open(here + '\\texts\sword-blades-and-poppy-seed.txt').read()
amores = open(here + '\\texts\\amores.txt').read()


#Using poetry class:
#p = poetry.Poetry('data2.txt')
#p.export_collection('data2-results')
#p.print_poem(4, 10, 2, 1)
#p.json_collection('November 4th')

def demo():
    p1 = poetry.Poetry('data3.txt')
    p1.json_collection('Day Poetry')
    print('Set poetry for daytime')
    f = input("\nContinue?\n")
    if f == '':
        p2 = poetry.Poetry('data1.txt')
        p2.json_collection('Night Poetry')
        print('Set poetry for nighttime')
#demo()
p = poetry.Poetry('data2.txt')
p.json_collection('Test')

def run_w_input():
    #add dataset input
    p = poetry.Poetry('data3.txt')
    while(True):
        f = input("\nEnter a function: ")
        if 'set data ' in f:
            name = f.split('data ', 1)[1].strip()
            if not name:
                print('\nError: needs name for file')
            else:
                p = poetry.Poetry(name+'.txt')
                print('\nData set to \'data1.txt\'')
        elif f == 'print poem':
            p.print_poem()
        elif f == 'print collection':
            p.print_collection()
        elif 'export collection ' in f:
            name = f.split('collection ', 1)[1].strip()
            if not name:
                print('\nError: needs name for file')
            else:
                p.export_collection(name)
        elif f == 'exit':
            break;
        else:
            print('\nError: function does not exist')

#run_w_input()

#bright = [x[1] for x in p1.data]
#temp = [x[0] for x in p1.data]
#print(bright)
#print(temp)


#bright_range = max(bright) - min(bright)
#print(bright_range)

#temp_range = max(temp) - min(temp)
#print(temp_range)
#min poem len: 3 lines of 7
#max poem len: 4 stanzas of 4 of 10

#t = re.sub(r'     I..', '     ', t)
#print(re.sub(r'     V...', '     ', t))




#go through all corpora
#read rules
#don't do strict line lengths
#format poems
#package everything correctly
#github
#refactor loading in new texts to main file (or poetry???)














#TODO
#implement backtracking
#   diff levels of grammar chunking
#   can be refined by chinking (rem from chunk)

#sometimes use rules, randomize when they happen
#   repetition of words, rhyming