# coding=utf-8

from pymongo import MongoClient
import pandas as pd

client = MongoClient()
collection = client["jd"]["comments"]
data = collection.find()

data_list = []
for i in data:
    item = {"id": i["id"], "date": i["date"], "nickname": i["nickname"]}
    data_list.append(item)

df = pd.DataFrame(data_list)
# print(df)

# print(list(data))
# t1 = data[0]
# t1 = pd.Series(t1)
# print(t1)

#显示头几行
print(df.head(3))
print("*"*100)
#显示尾几行
print(df.tail(2))

#展示df的概览
# print(df.info())
# print(df.describe())
# print(df["nickname"].str.split("/").tolist())