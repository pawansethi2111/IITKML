class spamFilter2:

    def create_freq_table():
        freq_table={}
        for tok in tok_array:

            entry={}
            spam_freq = self.len(spam_table)
            entry['spam_freq'] = spam_freq

            ham_freq = self.len(ham_table)
            entry['ham_freq'] = ham_freq

            prob_spam = self.((spam_freq+1)/len(total_spam_toks+1))/(unique_s_toks+1)

            entry['prob_spam']= prob_spam

            prob_ham = self.((ham_freq)/len(total_ham_toks+1))/(unique_h_toks+1)

            entry['prob_ham'] = prob_ham

            freq_table[tok] = entry

    return freq_table


    def __init__(self,training_dir)

        print("Training filter with known ham")

        self.spam_table = dict(Counter(dir_tokens(training_dir + "spam/")))

        self.ham_table = dict(Counter(dir_tokens(training_dir + "ham/")))

        self.unique_s_toks = len(self.spam_table)

        self.unique_h_toks = len(self.ham_table)

        self.total_h_toks = sum(self.ham_table_values())

        self.total_s_toks = sum(self.spam_table_values())

        self.tok_arr = sorted(list(self.ham_table.keys()) + list(self.spam_table.keys()))

        self.freq_tab = self.create_frequency_table()

        self.file_count =0

        self.count_spam = 0

        self.count_ham =0

        self.ham_list=[]

        self.spam_list =[]



    def createfrequencytable():

        freq_table ={}

        for tok in self.toks_arr:

            entry{}

            s_freq = self.spam_table.get(tok,0)

            entry['freq'] = s_freq;

            h_freq = self.ham_table.get(tok,0)

            entry['freq2'] = h_freq;

            s_prob=(s_freq+1)/float()

    from  collections import Counter
    import math
    import os
    import re


    #def __init__(self,training_dir)
        #initialize
    def createfrequencytable(self)
        #entry =[]
        #frequency_table =[]
    3)def prob_spam(self,token)
        #upar wale se dalde ya fir 1/uniq_soks)(total_stoks+1)
    4)def prob_ham(self,token)

    5)def prob_spam(self,token)

    6)def prob_msg_spam(self,filepath)
        #sum += math.log10(prob_ham(tok)
    7)def prob_msg_ham(self,filepath)
        #sum +=math.log10(prob_ham(tok)

    8)def cleantable(self,min_frequency)
        #k,v in freq_tables.items()
        #frq_spam+freq_ham < min freq or 0.45<prob_spam)/(probspam+probham)<0.55
        #to k eppnd karde into rmkeys
        #for k in rmkeys
        #delete freq_tab[k]

    9)def printtable_info(self)

    10)def cleansplit(in_str)


    11)def tokens(text,tok_size=3)

    12)def dir_token(dir_path)

    13)def file_token(filepath)


    14)def classify(self,filepath)

    15)def classifyall(self,dirpath, known_type ="spam")

