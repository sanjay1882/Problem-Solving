a=list("534976")

i=len(a)-2

while i>=0 and a[i]>=a[i+1]:
   
    i-=1
j=len(a)-1
while a[j]<a[i]:
    j-=1


a[i],a[j]=a[j],a[i]
a[i+1:]=reversed(a[i+1:])
out="".join(a)
print(out)
