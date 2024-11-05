start=int(input())
end=int(input())
for i in range(start,end+1):
    if i%2 != 0:
        rev=int(str(i)[::-1])
        if rev==i:
            print(i,end=" ")