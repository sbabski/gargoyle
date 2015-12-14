import nltk

def tabulate(cfdist, words, categories):
    # column headings
    print('{:16}'.format('Category'), end=' ')
    for word in words:
        print('{:>6}'.format(word), end=' ')
    print()
    for category in categories:
        #row heading
        print('{:16}'.format(category), end=' ')
        for word in words:
            # table cell
            print('{:6}'.format(cfdist[category][word]), end=' ')
        print()

from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
#tabulate(cfd, modals, genres)


#Test 1:
data1 = open(here + '\data.txt').read()
d1 = data1.split('\n')
d1 = [[float(i) for i in x.split(' ')] for x in data1.split('\n')[:-1]]
#print(d1[len(d1)-1])
m1 = markov.Markov(poppy, 'poppy', 8, 10)
#Generation
poem1 = m1.generate()
print('Poem 1: generated at 60 degrees, high brightness\n'+poem1)
t = nltk.pos_tag(word_tokenize(poem1))
#print(t)


#Test 2:
data2 = open(here + '\data2.txt').read()
d2 = data2.split('\n')
d2 = [[float(i) for i in x.split(' ')] for x in data2.split('\n')[:-1]]
#print(d2[len(d2)-1])
m2 = markov.Markov(pastoral, 'pastoral', 3, 7)
#Generation
poem2 = m2.generate()
print('\n\nPoem 2: generated at 76 degrees, low brightness\n'+poem2)