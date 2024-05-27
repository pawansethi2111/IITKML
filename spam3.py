from collections import Counter
import math
import os
import re

class Spamfilter(self):
    def init(self,dir_path):
        self.st = dict(Counter(dir_tok(dir_path  + "spam/")))
        self.ht  = dict(Counter(dir_tok(dir_path + "ham/")))
        self.tst = sum(self.st.values())
        self.tht = sum(self.ht.values())
        self.ust = len(self.st.keys())
        self.uht = len(self.ht.keys())
        self.freq_table = self.create_freq_table()
        self.tlist = sorted(list(self.ht.keys())+ list(self.st.keys()))


