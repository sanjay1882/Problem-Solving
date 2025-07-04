
s1="title"
s2="paper"
def pattern(s1):
    li=[s1.index(i) for i in s1]
    return li
print(pattern(s2)==pattern(s1))
