from collections import Counter
import math
import os
import re

class spamfilter:
    def __init__(self,dir_path):
        self.st = dir(Counter(self.dtok(dir_path+"spam/")))
        self.ht = dir(Counter(self.dtok(dir_path+"ham/")))
        self.uht = len(self.ht)
        self.ust = len(self.st)
        self.tst = sum(self.st.values())
        self.tht = sum(self.ht.values())
        self.freqtab = self.create_freq_table()
        self.tlist = sorted(list(self.ht.keys()) + list(self.st.keys()))
        self.fc=0
        self.cs=0
        self.ch=0
        self.hlist=[]
        self.slist=[]

    def create_freq_table(self):
        freqtab={}

        for tok in range(len(self.tlist)):
            entry={}
            sfreq = self.st.get(tok,0)
            entry['sfreq'] = sfreq

            hfreq = self.ht.get(tok,0)
            entry['hfreq'] = hfreq

            sprob = (sfreq+1/self.ust)/(self.tst+1)
            entry['sprob'] = sprob

            hprob = (hfreq+1/self.uht)/(self.tht+1)
            entry['hprob'] = hprob

            freqtab[tok] = entry

        return freqtab

    def sp(self,tok):

        val = self.freqtab.get(tok)
        if val is not None:
            return val['sprob']
        else:
            return (1/self.ust)/(self.tst+1)


    def hp(self,tok):
        val = self.freqtab.get(tok)

        if val is not None:
            return val['hprob']
        else:
            return(1/self.uht)/(self.tht+1)



    def hamlog(self,filepath):

        toks = self.ftok(filepath)
        for tok in toks:

            sum += math.log10(self.sp(toks))








