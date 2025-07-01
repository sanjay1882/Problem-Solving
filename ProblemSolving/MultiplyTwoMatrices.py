a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]

out=[[0]*len(a[0]) for _ in range(len(a))]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            out[i][j]+=a[i][k]*b[k][j]

print(out)
