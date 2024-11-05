def ispalin(s):
    rev=s[::-1]
    if rev==s:
        return 1
    return 0
s=input()
palin=''
max_length=0
for i in range(0,len(s)):
    for j in range(i,len(s)):
        word=s[i:j]
        if(ispalin(word)==1):
            if(max_length<len(word)):
                max_length=len(word)
                palin=word
print(palin)