def isprime(n):
    if n==0 or n==1:
        return 0
    for i in range(2,int(n//2 +1)):
        if n%i==0:
            return 0
    return 1

def prime_factorisation(n):
    l=[]
    for i in range(2,n+1):
        if isprime(i)==1:
            temp=n
            while(temp%i==0):
                l.append(i)
                temp=int(temp//i)
    return l

n=int(input())
print(prime_factorisation(n))