#[4,6,7,2,9] ans=2
def smash(stone):
    stone=sorted(stone,reverse=True)
    while(len(stone)>1):
        stone.append(stone.pop(0)-stone.pop(0))
        stone=sorted(stone,reverse=True)
    return stone[0]
    
stone=list(map(int,input().split()))
res=smash(stone)
print(res)