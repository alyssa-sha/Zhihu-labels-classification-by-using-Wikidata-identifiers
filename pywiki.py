import requests
import pandas as pd

#create the header you want to use
my_headers = {
    "User-Agent": "",
    "Accept": "application/json",
    "Connection": "close",
    "Cookie": ""}

"""extract a selected level of leaf entities from wikidata following P279""" 
def parent_items(level, headers):
    result_list = []
    id_data = pd.read_excel(str(level) + "parent_of_base.xlsx")
    df = pd.DataFrame(id_data, columns=[str(level) + 'parentid'])
    id_list = df.values.tolist()
    for id in id_list:
        hpCharURL = """https://query.wikidata.org/sparql?query= SELECT ?item ?itemLabel ?cls ?clsLabel WHERE {
          BIND(wd:""" + id[0] + """ AS ?item)
          ?item wdt:P279 ?cls.
          SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        GROUP BY ?item ?itemLabel ?cls ?clsLabel"""

        res = requests.get(hpCharURL, headers=headers).json()
        if res["results"]["bindings"] == []:
            pass
        else:
            for row in res["results"]["bindings"]:
                tdict = {"id": id[0],
                         "label": row["itemLabel"]["value"],
                         "cls": row["cls"]["value"],
                         "clsLabel": row["clsLabel"]["value"]}
                result_list.append(tdict)
                print(len(result_list))
    return result_list

"""collect and save the outputs into an excel"""
def generate_output(level, result):
    df_marks = pd.DataFrame(result)
    writer = pd.ExcelWriter(str(level) + "parent_of_base.xlsx")
    df_marks.to_excel(writer)
    writer.save()


#level = 7
#generate_output(level + 1, parent_items(level, my_headers))
