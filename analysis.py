import pandas as pd
import requests
#import datetime
#from bs4 import BeautifulSoup as bs
#import collections

df = pd.read_excel("~/Documents/data/Phosphopeptide files/QE013961ECDM prot.xlsm")



columns = df.columns.values      #list of column names
light = df.loc[:, "Abundances (Grouped): F1, Light"]       #list of Descriptions
heavy = df.loc[:, "Abundances (Grouped): F1, Heavy"]

#with open('labels.txt', 'w') as f:
#    for column in columns:
#        f.write('%s\n'%column)

protein = "Q9NUU7"
if __name__ == "__main__":
    url = "https://rest.uniprot.org/uniprotkb/search?query=" + protein
    results = requests.get(url).json()["results"]
    accession = results[0]["primaryAccession"]
    name = results[0]["proteinDescription"]["recommendedName"]["fullName"]["value"]
    seq = results[0]["sequence"]
    #sp = bs(r.text, "xml")
    #obj = r.text.split("{")
    #order = collections.OrderedDict(r.json())
    #keys = list(order)
    print(results[0]["proteinDescription"])



