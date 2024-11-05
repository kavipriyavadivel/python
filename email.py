mail=input()
n=len(mail)
i=0
while(i<n and mail[i]!='@'):
    i+=1
if i>=3:
    mail_list=list(mail)
    for j in range(1,i-1):
        mail_list[j]='*'
    mail=''.join(mail_list)
print(mail)