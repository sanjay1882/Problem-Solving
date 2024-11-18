import re
from collections import Counter
paragraph=""
banned=['']
r=re.findall(r'\w+',paragraph.lower())
print(r)
s=set(banned)
r=Counter(word for word in r if word not in s)
print(max(r,key=r.get))
