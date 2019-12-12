from fuzzywuzzy import fuzz
from fuzzywuzzy import process
d = []
f = input()
g = ['холодная вода на кухне', 'горячая вода на кухне',
     'горячая вода в туалете', 'холодная вода в туалете', 'электричество']
for i in g:
    s = fuzz.ratio(i, f)
    if s >= 80:
        print(i)
        d.append(i)
        print(f)
# 9 нулей максимум
