def main():
    k0 = eval(input("enter 10 numbers"))
    m1 = int(input("enter mean1"))
    m2 = int(input("enter mean2"))
    while True:
        om1 = m1
        om2 = m2
        k1=[]
        k2=[]
        for x in range(len(k0)):
            t1 = k0[x] - m1
            if t1 < 0:
                t1 = t1*-1
            t2 = k0[x] - m2
            if t2 < 0:
                t2 = t2*-1
            if t1 < t2:
                k1.append(k0[x])
            else:
                k2.append(k0[x])
        sum1=0
        for x in range(len(k1)):
            sum1 += k1[x]
        m1 = sum1/len(k1)
        sum2 = 0
        for x in range(len(k2)):
            sum2 += k2[x]
        m2 = sum2/len(k2)
        print("Cluster one : ",k1)
        print("Mean one : ",m1)
        print("Cluster Two : ",k2)
        print("Mean Two : ",m2)
        if m1 == om1 and m2 == om2:
            break
main()
