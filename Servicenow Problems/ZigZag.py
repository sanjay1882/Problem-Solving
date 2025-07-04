a=16
val=0
inc=0
k=3

b="paypalhere"

List=[[] for i in range(k)]
out=""
for i in range(len(b)):
    val+=inc
    List[val].append(b[i])
    if val==k-1:
        inc=-1
    if val==0:
        inc=1
for i in List:
    out+="".join(i)
print(out)