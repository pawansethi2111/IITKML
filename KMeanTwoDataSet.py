
def main():
    K0 = eval(input("Enter the list of 10 numbers "))
    M1 = int(input("Enter Mean 1 : "))
    M2 = int(input("Enter Mean 2 : "))
    while True:
        om1 = M1
        om2 = M2
        K2 = []
        K3 = []
        for i in range(len(K0)):
            t1 = K0[i]-M1
            if t1 < 0:
                t1 = t1 * -1
            t2 = K0[i]-M2
            if t2 < 0:
                t2 = t2 * -1
            if t1 < t2:
                K2.append(K0[i])
            else:
                K3.append(K0[i])
        sum1 = 0
        for i in range(len(K2)):
            sum1 += K2[i]
        M1 = sum1 / len(K2)
        print("Cluster one : ",K2)
        print("Mean one is ",M1)

        sum2 = 0
        for i in range(len(K3)):
            sum2 += K3[i]
        M2 = sum2 / len(K3)
        print("Cluster Two : ",K3)
        print("Mean two is : ",M2)
        if om1 == M1 and om2 == M2:
            break
main()