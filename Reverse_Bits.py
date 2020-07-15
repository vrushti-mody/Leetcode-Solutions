# Reverse bits of a given 32 bits unsigned integer.

n=str(bin(n))
        a=""
        for i in range(0,len(n)-2): 
            a = a + n[len(n)-i-1]
        for i in range(len(n)-2,32):
            a=a+"0"
        print(a)
        return int(a,2)
