# coding=utf-8

from matplotlib import pyplot as plt

#  设置图片大小
fig = plt.figure(figsize=(15,8),dpi=80)

x = range(2,26,2)
y = [22,15,6,36,8,13,9,26,31,33,16,29]

#  绘图
plt.plot(x,y)

#  设置x轴刻度
plt.xticks(x[::2])

#  保存图片
plt.savefig("./save.png")

#  展示图片
plt.show()
