from fuzzywuzzy import fuzz
from fuzzywuzzy import process
g = ['dsvsfgvs', 'dfvsgbwevsdfws', 'ghfuhfkjouidshkjsd', 'Привет 9009']
for i in g:
    s = fuzz.ratio('Привет', i)
    print(s)
