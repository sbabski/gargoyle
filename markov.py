import nltk
import os.path
import pickle
import random
from nltk.tokenize import word_tokenize

class Markov(object):

    def __init__(self, text, filename, lines, line_size, revised_text=False):
        self.text = text
        self.filename = filename
        if revised_text:
            os.remove(filename)
        self.file_data = self.initialize()
        self.token_text = self.file_data[0]
        self.tag_text = self.file_data[1]
        self.db = self.file_data[2]
        self.lines = lines
        self.line_size = line_size

    def initialize(self):
        if not os.path.isfile(self.filename):
            data = self.markov_format(self.text)
            self.export(data)
            return data
        else:
            return pickle.load(open(self.filename, 'rb'))

    def export(self, data):
        pickle.dump(data, open(self.filename, 'wb'))

    def markov_format(self, text):
        tokened = word_tokenize(text)
        tagged = nltk.pos_tag(tokened)
        tripled = {}
        for w1, w2, w3 in self.triple_gen(tagged):
            key = (w1,w2)
            if key in tripled:
                tripled[key].append(w3)
            else:
                tripled[key] = [w3]
        out = [tokened, tagged, tripled]
        return out

    def triple_gen(self,text):
        if len(text) < 3:
            return text
        for i in range(len(text) - 2):
            yield(text[i], text[i+1], text[i+2])

    def generate(self):
        while(True):
            seed = random.randint(0,len(self.token_text)-3)
            seed_word = self.tag_text[seed]
            if(seed_word[1].isalpha() and seed_word[0][0]!='\''):
                break
        next_word = self.tag_text[seed+1]
        w1, w2 = seed_word, next_word
        word_index = -1
        gen_words = []
        for i in range(self.lines * self.line_size -1):
            word_index +=1
            if word_index >= self.line_size and w1[0][0].isalpha():
                word_index = 0
            gen_words.append(self.format(w1, word_index))
            w1, w2 = w2, random.choice(self.db[(w1, w2)])
        gen_words.append(self.format_last(self.format(w2, word_index+1),w2[1]))
        return ''.join(gen_words)

    def format(self, word, index):
        #out = word[0]+str(index)
        #do differently for parens
            #mark front paren index, must have back
            #also space correctly
        #mark sentences
            #can capitalize first word correctly
        #out[0]!='\'' cannot be first word
        out = word[0]
        if index == 0:
            out = '\n' + out[0].upper()+out[1:].lower()
        else:
            if out != 'I':
                #out = out
                out = out.lower()
            if out == '(' or (word[1][0].isalpha() and out[0] != '\''):
                out = ' '+ out
        return out

    def format_last(self, word, pos):
        bad_pos = ['DT', 'CC', 'PRP', 'JJ', 'IN', 'WRB', 'RB', 'TO']
        out = word
        if 'PRP' in pos or 'RB' in pos:
            while(True):
                seed = random.randint(0,len(self.token_text)-3)
                verb = self.tag_text[seed]
                if('V' in verb[1]):
                    break
            out =  out+' '+verb[0]
        elif 'NN' not in pos and 'V' not in pos and pos[0].isalpha():
            while(True):
                seed = random.randint(0,len(self.token_text)-3)
                noun = self.tag_text[seed]
                if('NN' in noun[1]):
                    break
            out = out+' '+noun[0]
        #if pos[0].isalpha() or pos == 'CC':
        #    for p in bad_pos:
        #        if pos == p:
        #            out = out + ' bad'
                    #out = out
        #else:
        #    out = ''
        if ',' in out or ':' in out or '(' in out:
            out = ''
        return out
        #if end on bad, add until good