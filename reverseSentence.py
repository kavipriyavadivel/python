s=input()
l=s.split(' ')
i=0
j=len(l)-1
while(i<j):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    j-=1
    i+=1
s=' '.join(l)
print(s)
