s="LeetcodeHelpsMeLearn"
sp=[8,13,15]
l=list(s)
ind=0
for i in range(len(sp)):
    l.insert(sp[i]+ind,' ')
    ind+=1 
out="".join(map(str,l))
print(out)
print([0]+sp)
print(sp+[len(s)])
for i, j in zip([0]+sp, sp+[len(s)]):
    print(s[i:j],end=' ')