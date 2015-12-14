import os.path
import markov
import glob
import json
class Poetry(object):

    def __init__(self, datafile):
        self.here = os.path.dirname(os.path.realpath(__file__))
        file = open(self.here + '\\'+ datafile).read()
        self.data = \
            [[float(i) for i in x.split(' ')] for x in file.split('\n')]
        self.t_f = glob.glob(self.here+'\\texts\*.txt')
        self.c_f = glob.glob(self.here+'\\corpora\*.p')

    def gen_poem(self, lines=4, line_len=10, s=2, i=0, new=False):
        #m = markov.Markov(
        #    open(self.t_f[0]).read(),self.here+'\\corpora\\sea-garden.p', lines, line_len)
        m = markov.Markov(
            open(self.t_f[i]).read(),self.c_f[i], lines, line_len, new)
        out = ''
        for n in range(s):
            out = out + m.generate() + '\n'
        return out[:-1]

    def print_poem(self, lines=4, line_len=10, s=2, i=0, new=False):
        print(self.t_f[i])
        print(self.gen_poem(lines, line_len, s, i, new))

    def gen_collection(self):
        collection = ''
        for i in range(len(self.data)):
            temp = self.map_temp(self.data[i][0])
            bright = self.map_bright(self.data[i][1])
            m = self.gen_poem(bright[0], bright[1], bright[2], temp)
            collection = collection+ str(i+1) + '.' + m + '\n\n'
        return collection[:-2]

    def json_collection(self, name='Poetry Collection'):
        poems = []
        for i in range(len(self.data)):
            temp = self.map_temp(self.data[i][0])
            bright = self.map_bright(self.data[i][1])
            m = self.gen_poem(bright[0], bright[1], bright[2], temp)
            entry = {'index': self.romanize(i+1), 'words':m}
            poems.append(entry)
        self.create_json(poems, name)

    def create_json(self, poems, name='Poetry Collection'):
        data = {'name':name, 'poems':poems}
        with open(self.here+'\web\\p.json', 'w') as outfile:
            json.dump(data, outfile, sort_keys = True, indent = 4)
        print('Created collection as a json')

    def print_collection(self):
        print(self.gen_collection())

    def export_collection(self, name):
        with open(self.here+'\output\\'+name+'.txt', 'w') as text_file:
            print(self.gen_collection(), file = text_file)
            print('Done!\nFile location: \'\output\\'+name+'.txt\'')


    def map_bright(self, val):
        if val < 20: return [3, 7, 1]
        elif val < 40: return [7, 3, 1]
        elif val < 60: return [8, 8, 2]
        elif val < 80: return [10, 6, 1]
        else: return [12, 7, 3]

    def map_temp(self, val):
        if val < 62: return 6
        elif val < 65: return 0
        elif val < 68: return 5
        elif val < 71.5: return 1
        elif val < 74: return 4
        else: return 3

    def romanize(self, n):
        digits = [(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = ""
        while len(digits) > 0:
            (val, romn) = digits[0] # Unpacks the first pair in the list
            if n < val:
                digits.pop(0) # Removes first element
            else:
                n -= val
                result += romn
        return result