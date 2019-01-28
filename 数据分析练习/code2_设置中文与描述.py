# coding=utf-8
from matplotlib import pyplot as plt
import random
from matplotlib.font_manager import FontProperties


# 设置中文字体
font = FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc", size=10) #C:\WINDOWS\Fonts

fig = plt.figure(figsize=(15,10),dpi=80)
x = range(120)
random.seed(10)
y = [random.uniform(20,35) for i in range(120)]

plt.plot(x,y)

_x_ticks = ["10点{}分".format(i) for i in x if i<60]
_x_ticks += ["11点{}分".format(i-60) for i in x if i>60]

# 数字与字符串长度要一一对应
plt.xticks(x[::5], _x_ticks[::5], rotation=90,fontproperties=font)  # rotation设置旋转的度数，fontproperties应用字体格式

# 添加描述信息
plt.xlabel("时间", fontproperties=font)
plt.ylabel("温度", fontproperties=font)
plt.title("10点到12点每分钟气温的变化情况", fontproperties=font)

plt.show()
