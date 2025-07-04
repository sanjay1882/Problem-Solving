a=6
a=
dp=[1,2]

for i in range(2,a):
    dp.append(dp[-1]+dp[-2])
print(dp)


