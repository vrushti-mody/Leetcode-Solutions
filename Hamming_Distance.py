# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note: 0 ≤ x, y < 2 to the power 31.

def hammingDistance(self, x: int, y: int) -> int:
        a=bin(x)
        b=bin(y)
        a=a[2:]
        b=b[2:]
        count=0
        if (len(a)>=len(b)):
            s=""
            for i in range(0,len(a)-len(b)):
                s=s+"0"
            s=s+b
            for i in range(0,len(a)):
                if s[i]!=a[i]:
                    count=count+1
            return count   
        if (len(a)<len(b)):
            s=""
            for i in range(0,len(b)-len(a)):
                s=s+"0"
            s=s+a
            for i in range(0,len(b)):
                if s[i]!=b[i]:
                    count=count+1
            return count
        return count
