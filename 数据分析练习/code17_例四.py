# coding=utf-8

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


font = FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc", size=10) #C:\WINDOWS\Fonts
file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)
df = df[df["Country"] == 'CN']
print(df)

#使用matplotlib呈现出店铺总数排名前10的国家
#准备数据

data = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:25]
# print(data)
# #画图
# _x = data.index
# _y = data.values
# print(_x,_y)
#
# plt.figure(figsize=(20,8), dpi=80)
#
# plt.bar(range(len(_x)), _y, color="orange")
#
# plt.xticks(range(len(_x)), _x, fontproperties=font)
#
# plt.show()
