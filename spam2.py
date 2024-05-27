from collections import Counter
import math
import os
import re

class Spamfilter():

    '''naive bayes spam filter'''
    def __init__ (self, path):
        self.ht = dict(Counter(dtok(path+"ham/")))
        self.st = dict(Counter(dtok(path+'spam/')))
        self.uht = len(self.ht)
        self.ust = len(self.st)
        self.tht = sum(self.ht.values())
        self.tst = sum(self.st.values())
        self.tList = sorted(list(self.ht.keys()) + list(self.st.keys()))
        self.ft = self.create()
        self.fc = 0
        self.cs = 0
        self.ch = 0
        self.slist = []
        self.hlist = []

    def create(self):
        ftab = {}
        for tok in self.tList:
            value = {}
            sf = self.st.get(tok, 0)
            value['sfreq'] = sf
            hf = self.ht.get(tok, 0)
            value['hfreq'] = hf
            sp = (sf + 1 / float(self.ust)) / (self.tst + 1)
            value['sprob'] = sp
            hp = (hf + 1 / float(self.uht)) / (self.tht + 1)
            value['hprob'] = hp
            ftab[tok] = value
        return ftab

    def sp(self, tok):
        val = self.ft.get(tok)
        if val is not None:
            return val['sprob']
        else:
            return (1.0 / self.ust) / (self.tst + 1)

    def hp(self, tok):
        val = self.ft.get(tok)
        if val is not None:
            return val['hprob']
        else:
            return (1.0 / self.uht) / (self.tht + 1)

    def spamlog(self, path):
        toks = ftok(path)
        sum = 0
        for tok in toks:
            sum += math.log10(self.sp(tok))
        return sum

    def hamlog(self, path):
        toks = ftok(path)
        sum = 0
        for tok in toks:
            sum += math.log10(self.hp(tok))
        return sum

    def classify(self, path):
        self.fc += 1
        if self.spamlog(path) > self.hamlog(path):
            self.cs += 1
            self.slist.append(path)
            return True
        else:
            self.ch += 1
            self.hlist.append(path)
            return False

    def classify_all(self, path, type='spam'):
        self.hlist = []
        self.slist = []
        self.fc = 0
        self.cs = 0
        self.ch = 0

        try:
            for f in os.listdir(path):
                self.classify(path + f)
                if type == 'spam':
                    correct = self.cs / float(self.fc)
                else:
                    correct = self.ch / float(self.fc)
            print("Correct: {:6.2f}%".format(correct * 100))
        except FileNotFoundError as e:
            print("ERROR: " + str(e))



    def clean_table(self, min_freq):
        rm_keys = []
        for k, v in self.ft.items():
            if (v['sfref'] + v['hfreq'] < min_freq or 0.45 < (v['sprob'] / (v['sprob'] + v['hprob'])) < 0.55):
                rm_keys.append(k)
        for k in rm_keys:
            print("deleting " + str(k) + " from freq table in clean()")
            del self.ft[k]

    def clean_split(str):
        return re.sub(r'[^\s\w]|_', '', str).lower().split()

    def ftok(path):
        tok = []
        try:
            with open(path, encoding="utf8", errors='ignore') as file:
                for f in file:
                    word = clean_split(f)
                    tok.extend(word)
        except FileNotFoundError as e:
            print("Error:" + str(e))
        return [x for x in tok if len(x) < 10]

    def dtok(path):
        d = []
        try:
            file = os.listdir(path)
            for f in file:
                d.extend(ftok(path + f))
        except FileNotFoundError as e:
            print("Error:" + str(e))
        return d



if __name__ == " main ":
    sf = Spamfilter('emails_small/training/') # Object create
    #sf.print_table_info()
    sf.classify_all("emails_small/testing/spam/", 'spam')
    sf.classify_all("emails_small/testing/ham/", 'ham')
