# coding=utf-8

# 英国和美国各自youtube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图

import numpy as np
from matplotlib import  pyplot as plt

us_file_path = "./US_video_data_numbers.csv"
uk_file_path = "./GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t_us = np.loadtxt(us_file_path,delimiter=",",dtype="int")

#取评论的数据
t_us_comments = t_us[:,-1]

#选择比5000小的数据
t_us_comments = t_us_comments[t_us_comments<=5000]

print(t_us_comments.max(),t_us_comments.min())

d = 50  # 组距

bin_nums = (t_us_comments.max()-t_us_comments.min())//d  # 组数

#绘图
plt.figure(figsize=(20,8),dpi=80)

plt.hist(t_us_comments,bin_nums)

plt.show()
