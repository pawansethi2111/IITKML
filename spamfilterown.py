from collections import Counter
import math
import os
import re

class Spamfilter:
    def __init__(self,training_dir):
        self.st = dir(Counter(self.dtok(training_dir  + "spam/")))
        self.ht = dir(Counter(self.dtok((training_dir + "ham/"))))
        self.ust = len(self.st)
        self.uht = len(self.ht)
        self.tst = sum(self.st.values())
        self.tht = sum(self.ht.values())
        self.ftable = self.create_freq_table()
        self.tlist = sorted(list(self.ht.keys())+ list(self.st.keys()))
        self.cs =0
        self.ch=0
        self.fc=0
        self.hlist=[]
        self.slist=[]

    def create_freq_table(self):
        freq_table = {}

        for tok in self.tlist:
            entry = {}
            sfreq = self.st.get(tok,0)
            entry['sfreq'] = sfreq

            hfreq = self.ht.get(tok,0)
            entry['hfreq'] = hfreq

            sprob = (self.sfreq+1/self.ust)/(self.tst+1)
            entry['sprob'] = sprob

            hprob = (self.hfreq+1/self.uht)/(self.tht+1)
            entry['hprob'] = hprob

            freq_table[tok] = entry
        return freq_table

    def sp(self,tok):
        val = self.ftable.get(tok)
        if val is not None:
            return val['sprob']
        else:
            return (1/self.ust)/(self.tst+1)

    def hp(self,tok):
        val = self.ftable.get(tok)
        if val is not None:
            return val['hprob']
        else:
            return (1/self.uht)/(self.tht+1)

    def spamlog(self,filepath):

        toks = self.ftok(filepath)
        sum = 0
        for tok in toks:

            sum += math.log10(self.sp(tok))
        return sum

    def hamlog(self,filepath):

        toks = self.ftok(filepath)
        sum=0
        for tok in toks:
            sum += math.log10(self.hp(tok))

        return sum


    def classify(self,filepath):
        self.fc+=1
        if self.spamlog(filepath)>self.hamlog(filepath):
            self.cs+=1
            self.slist.append(filepath)
            return True
        else:
            self.ch+=1
            self.hlist.append(filepath)
            return False


    def classifyall(self,dirpath,known_type='spam'):

        self.cs=0
        self.ch=0
        self.hlist=[]
        self.slist=[]
        self.fc=0
        try:
            file = os.listdir(dirpath)
            for f in file:
                self.classify(self.f)
                if known_type == 'spam':
                    correct = self.cs/float(self.fc)
                else:
                    correct = self.ch/float(self.fc)
        except FileNotFoundError as e:
            print("error is ->", str(e))

        return correct*100

    def cleantable(self,min_freq):
        rm_keys=[]

        for k,v in self.ftable.items():
            if v['sfreq'] + v['hfreq']< min_freq or 0.45 < v['sprob']/(v['sprob']+v['hprob']) < 0.55:
                rm_keys.append(k)


            for k in rm_keys:
                print('item deleted ->', str(k))
                del self.ftable[k]

    def clean_split(self,str):
        return re.sub(r'[^\s\w]|_' , '' , str)

    def ftok(self, filepath):

        toks=[]

        try:
            file = open(filepath,encoding = "utf-8", errors="ignore")
            for f in file:
                words = self.clean_split(f)
                toks.append(words)

        except FileNotFoundError as e:
            print(str(e))

        return [x for x in toks if len(x)<10]

    def dtok(self,dirpath):

        dtok=[]

        try:
            files = os.listdir(dirpath)
            for f in files:
                dtok.append(self.ftok(dirpath+f))

        except FileNotFoundError as e:
            print(str(e))

        return dtok

if  __name__=="main":

    sf = Spamfilter("email_small/training")
    #sf.printtable()
    sf.classifyall("email_small/testing/spam")
    sf.classifyall("email_small/testing/ham")










