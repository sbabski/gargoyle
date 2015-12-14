import nltk
from nltk.tokenize import word_tokenize
import os

here = os.path.dirname(os.path.realpath(__file__))
text1 = nltk.corpus.gutenberg.raw('milton-paradise.txt')
text2 = nltk.corpus.webtext.raw('overheard.txt')
text3 = open(here + '\corpora\hacker-bible.txt', encoding='utf-8').read()
data = open(here + '\data.txt').read()

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
grammar_first = "NP: {<DT>?<JJ.*>*<NN.*>}"

#deal with punctuation and CC
grammar = r"""
            NP: {<PRP.*|DT|JJ|NN.*>+}
            PP: {<IN><NP>}
            VP: {<EX>?<VB.*>?<VB.*><NP|PP|CLAUSE>+}
            CLAUSE: {<NP><PP>}
            """

cp = nltk.RegexpParser(grammar, loop=2)
parsed = cp.parse(sentence)
#print(parsed)
#parsed.draw()


l1 = 'All day it has rained, and we on the edge of the moors'
l2 = 'Have sprawled in our bell-tents, moody and dull as boors,'
l3 = 'Groundsheets and blankets spread on the muddy ground'
l4 = 'And from the first grey wakening we have found'
l5 = 'No refuge from the skirmishing fine rain'
l6 = 'And the wind that made the canvas heave and flap.'

m1 = 'Last night, ah, yesternight, betwixt her lips and mine'
m2 = 'There fell thy shadow, Cynara! thy breath was shed'
m3 = 'Upon my soul between the kisses and the wine;'
m4 = 'And I was desolate and sick of an old passion,'
m5 = 'Yea, I was desolate and bowed my head:'
m6 = 'I have been faithful to thee, Cynara! in my fashion.'
lines = [l1,l2,l3,l4,l5,l6]
lines = [m1,m2,m3,m4,m5,m6]
result = [cp.parse(nltk.pos_tag(word_tokenize(l))) for l in lines]
for r in result:
    print(r)
#print(result)
s2 = nltk.pos_tag(word_tokenize(l1))
print(cp.parse(s2))