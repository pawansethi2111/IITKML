
import csv
class Spamfilter():

    '''naive bayes spam filter'''
    def filter(self, data):
        f = open(data,"r")
        csvreader = csv.reader(f)
        dataset = list(csvreader)
        self.spam_table = {}
        self.ham_table = {}
        for r in dataset:
            if r[1] == 'ham':
                if r[0] in self.ham_table:
                    self.ham_table[r[0]] += 1
                else:
                    self.ham_table[r[0]] = 1
            elif r[1] == 'spam':
                if r[0] in self.spam_table:
                    self.spam_table[r[0]] += 1
                else:
                    self.spam_table[r[0]] = 1

    def __init__ (self, training_dir):
        print('Training filter with known ham ...')

        self.filter(training_dir)
        self.uniq_h_toks = len(self.ham_table)
        self.uniq_s_toks = len(self.spam_table)
        self.total_h_toks = sum(self.ham_table.values())
        self.total_s_toks = sum(self.spam_table.values())
        self.tok_arr = sorted(list(self.ham_table.keys()) + list(self.spam_table.keys()))

        self.file_count = 0
        self.count_spam = 0
        self.count_ham = 0
        self.spam_list = []
        self.ham_list = []

    def classify_all(self, dir_path, known_type='spam'):
        try:
            self.ham_list = []
            self.spam_list = []
            self.file_count = 0
            self.count_spam = 0
            self.count_ham = 0
            f = open(dir_path,"r")
            csvreader = csv.reader(f)
            dataset = list(csvreader)
            self.file_count = len(dataset)-1
            for i in dataset:
                if i[1] == 'ham':
                    self.count_ham += 1
                    self.ham_list.append(i[0])
                elif i[1] == 'spam':
                    self.count_spam += 1
                    self.spam_list.append(i[0])


            if known_type == 'spam':
                correct = self.count_spam / float(self.file_count)
            else:
                correct = self.count_ham / float(self.file_count)
            print('Total spam', self.count_spam)
            print('Total ham',  self.count_ham)
            print("Correctly classified: {:6.2f}%".format(correct * 100))
        except FileNotFoundError as e:
            print("ERROR: classify_all() failed " + str(e))
    def print_table_info(self):
        print('\n=======================================')
        print('TRAINING AND FREQUENCY TABLE INFO')
        print("=======================================")
        print('Unique tokens in spam messages:{:8d}'.format(len(self.spam_table)))
        print('Unique tokens in ham messages: {:8d}'.format(len(self.ham_table)))
        print('Unique tokens in ALL messages: {:8d}'.format(self.file_count))
        print('Num spam e-mails:{:22d}'.format(len(self.spam_list)))
        print('Num ham e-mails: {:22d}'.format(len(self.ham_list)))

def main():
    sf = Spamfilter('spam_ham_dataset.csv') # Object create

    sf.classify_all("spam_ham_dataset.csv", 'spam')
    sf.classify_all("spam_ham_dataset.csv", 'ham')
    sf.print_table_info()
main()