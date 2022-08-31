import requests
import json
import pandas as pd
import time
id_data= pd.read_excel("7parent_of_base.xlsx")
df=pd.DataFrame(id_data,columns=['7parentid'])
id_list=df.values.tolist()
result_list=[]

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50",
            "Accept": "application/json",
            "Connection": "close",
            "Cookie":"GeoIP=AU:ACT:Canberra:-35.28:149.13:v4; WMF-Last-Access=20-Oct-2021; WMF-Last-Access-Global=20-Oct-2021"}

for id in id_list:
    # try:
    hpCharURL = """https://query.wikidata.org/sparql?query= SELECT ?item ?itemLabel ?cls ?clsLabel WHERE {
      BIND(wd:"""+id[0]+""" AS ?item)
      ?item wdt:P279 ?cls.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    GROUP BY ?item ?itemLabel ?cls ?clsLabel"""

    res = requests.get(hpCharURL, headers=headers).json()
    if res["results"]["bindings"]==[]:
        pass
    else:
        for row in res["results"]["bindings"]:
            tdict = {"id":id[0],
                   "label":row["itemLabel"]["value"],
                   "cls": row["cls"]["value"],
                   "clsLabel": row["clsLabel"]["value"]}
            result_list.append(tdict)
            print(len(result_list))
    # except ValueError:
    #     print("jasonDecodeError")
    #     continue

df_marks = pd.DataFrame(result_list)
writer = pd.ExcelWriter("8parent_of_base.xlsx")
df_marks.to_excel(writer)
writer.save()