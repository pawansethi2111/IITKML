import csv
class Spamfilter():
    def filter(self, training_dir):
        file = open(training_dir,'r')
        csvfile = csv.reader(file)
        dataset = list(csvfile)
        self.st={}
        self.ht={}
        for x in dataset:
            if x[1] =="spam":
                if x[0] in self.st:
                    self.st[x[0]]+=1
                else:
                    self.st[x[0]]=1
            elif x[1] =="ham":
                if x[0] in self.ht:
                    self.ht[x[0]]+=1
                else:
                    self.ht[x[0]]=1

    def __init__ (self,training_dir):

        self.filter(training_dir)
        self.ust = len(self.st)
        self.uht = len(self.ht)
        self.tst = sum(self.st.values())
        self.tht = sum(self.ht.values())
        self.tlist = sorted(list(self.st.keys()) + list(self.ht.keys()))
        self.fc=0
        self.cs=0
        self.ch=0
        self.hlist=[]
        self.slist=[]

    def classifyall(self,dir_path,known_type = 'spam'):


        try:
            self.fc=0
            self.cs=0
            self.ch=0
            self.hlist=[]
            self.slist=[]
            file = open(dir_path,"r")
            csvfile = csv.reader(file)
            dataset = list(csvfile)
            self.fc = len(dataset)-1
            for x in dataset:
                if x[1] =="spam":
                    self.slist.append(x[0])
                    self.cs+=1

                elif x[1]== "ham":
                    self.hlist.append(x[0])
                    self.ch+=1
            if known_type == "spam":
                correct = self.cs/self.fc
            else:
                correct = self.ch/self.fc

        except FileNotFoundError as e:
            print(str(e))

    def print_table_info(self):
        print("unique spam tokens", len(self.st))
        print("unique ham tokens", len(self.ht))
        print("File count", self.fc)
        print("Num spam email messages", len(self.slist))
        print("num ham email messages", len(self.hlist))
        print('Total spam', self.cs)
        print('Total ham', self.ch)


def main():
    sf = Spamfilter("spam_ham_dataset.csv")
    sf.classifyall("spam_ham_dataset.csv", "spam")
    sf.classifyall("spam_ham_dataset.csv", "ham")
    sf.print_table_info()
main()











