import requests
import json
from pprint import pprint
api = "http://join.navgurukul.org/api/partners"
url = requests.get(api)
data = url.json()
with open("parent.json","w") as saral:
    json.dump(data,saral,indent = 4)
id = []
def partner_name():
  j = 0
  while j < len(data["data"]):
      partner_name = data["data"][j]["name"]
      partner_id = data["data"][j]["id"]
      id.append(partner_id)
      print(j+1,partner_name,"Id",partner_id)
      j = j + 1
partner_name()
i = 0
while i < len(id):
    j = 0
    while j < len(id):
        if id[i] < id[j]:
            a = id[i]
            id[i] = id[j]
            id[j] = a
        j = j + 1
    i = i + 1
def assending_descending():
    list1 = []
    next = input("how you want data a for assending or d for descending :")
    if next == "a":
        l = 0
        while l < len(id):
            k = 0
            while k < len(data["data"]):
                if id[l] == data["data"][k]["id"] :
                    list1.append(data["data"][k])
                k = k + 1
            l = l + 1
        with open("assending_order_viva_id.json","w") as text_data:
            json.dump(list1,text_data,indent = 4)
    elif next == "d":
        l =  1
        while l <= len(id):
            k = 0
            while k < len(data["data"]):
                if id[-(l)] == data["data"][k]["id"] :
                    list1.append(data["data"][k])
                    print(id[-l])
                k = k + 1
            l = l + 1
        with open("dessending_order_viva_id.json","w") as text_data:
            json.dump(list1,text_data,indent = 4)
    else:
        print("invalid!,you select invalid input ")
assending_descending()
    