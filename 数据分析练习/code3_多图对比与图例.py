# coding=utf-8

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


# 设置中文字体
font = FontProperties(fname="C:\\WINDOWS\\Fonts\\simsun.ttc", size=10) #C:\WINDOWS\Fonts

fig = plt.figure(figsize=(15,10),dpi=80)
x = range(11,31)
y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2= [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

plt.plot(x,y,label="自己",color="red",linestyle="-.")  # 设置图形名称
plt.plot(x,y2,label="同桌",color="g",linestyle=":")

_x_ticks = ["{}岁".format(i) for i in x]

plt.xticks(x,_x_ticks,rotation=90,fontproperties=font)

plt.xlabel("年龄",fontproperties=font)
plt.ylabel("次数",fontproperties=font)
plt.title("恋爱走势",fontproperties=font)

# 绘制网格,alpha设置透明度
plt.grid(alpha=0.4)

# 添加图例
plt.legend(prop=font,loc="best")

plt.show()
