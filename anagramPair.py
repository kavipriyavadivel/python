l=input().split()
count=0
seen=set()
for i in range(0,len(l)):
    word1=''.join(sorted(l[i]))
    if word1 not in seen:
        for j in range(i+1,len(l)):
            word2=''.join(sorted(l[j]))
            if word1==word2:
                count+=1
                break
    seen.add(word1)
print(count)