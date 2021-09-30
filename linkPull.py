from os import fdopen
import pandas as pd
from pandas.core.arrays.sparse import dtype 
from serviceCodeMap import codeMap
import pickle


# required variables
urls = []
zipCityState = []
dtypeDic = {'zip': str}
df = pd.read_csv('zipCityState.csv', dtype=dtypeDic)
df = df[['zip', 'primary_city', 'state']]


# main URL construction loop
for index in range(len(df)):
    if df.iloc[index]['state'] == "PR":
        continue
    currentZip = df.iloc[index]['zip']
    while len(currentZip) != 5:
        currentZip = "0" + currentZip
    for service in codeMap:
        front = "https://www.homeadvisor.com/c." + service + "."
        back = df.iloc[index]['primary_city'] + "." + df.iloc[index]['state'] + ".-" + codeMap[service] + ".html?zipSearched=" + currentZip
        toAdd = front + back
        print(toAdd)
        urls.append(toAdd)

# dumping to file
with open('allLinks', 'wb+') as f:
    pickle.dump(urls, f)
