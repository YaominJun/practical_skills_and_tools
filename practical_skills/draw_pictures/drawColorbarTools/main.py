#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import path_Results as paths

#渐变色

#数据读取
# 1路径结果数据
result0 = pd.read_csv("mp_1.csv")
result1 = pd.read_csv("mp_2.csv")
result0 = result0.values
result1 = result1.values

#设置画布
width_img = 5
height_img = 5
fig = plt.figure(figsize=(int(width_img)+2, int(height_img)+2),
                 facecolor='none')
ax = plt.gca()
#设置图像上下界
plt.xlim(0,20)
plt.ylim(0,20)

#设置字体
font1 = {'family': 'Times New Roman','weight': 'normal', 'size': 15}
font2 = {'family': 'Times New Roman','fontstyle': 'italic', 'size': 15}
plt.tick_params(labelsize = 12)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#绘制路径结果轨迹
lc = paths.plot_results_path(result0,4)
lc2 = paths.plot_results_path(result1, 4)

#label
plt.xlabel('x [m]', font1)
plt.ylabel('y [m]', font1)

#绘制渐变色的图例
cb = paths.plot_gd_bar(fig, ax, lc, result0[-1, 2], 10) #最后两个参数一个是调整比例，一个是调整偏移量
plt.text(ax.get_position().x1,
         ax.get_position().y0 - 0.25, 'v ', font2)
plt.text(ax.get_position().x1,
         ax.get_position().y0 - 0.25, ' [m/s]', font1)

plt.show()
