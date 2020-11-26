import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

import gradient as gd


def plot_results_path(result0_tmp, linewidth_car=4):
    x = result0_tmp[:, 0]
    y = result0_tmp[:, 1]
    z = result0_tmp[:, 2] / 20
    # 设置颜色渐变色
    # 'jet', 'cool'
    lc = gd.colorline(x, y, z, cmap=plt.get_cmap('cool'), linewidth=linewidth_car)  # 'jet' #'cool'
    return lc


def plot_gd_bar(fig, ax, lc, max_pro, max_tran=0, cars_num=1, car_num=0, offset=0):
    cax = fig.add_axes([ax.get_position().x1 + 0.01,
                        ax.get_position().y0 + (car_num / cars_num) * ax.get_position().height,
                        0.02,
                        ax.get_position().height - (
                                    (cars_num - car_num - 1) / cars_num) * ax.get_position().height - offset])
    cb = plt.colorbar(lc, cax=cax)

    # 调整渐变色图例显示数据范围
    def label_cbrt(x, pos):
        return "{:.1f}".format(max_pro * np.cbrt(x) + max_tran)

    cb.formatter = ticker.FuncFormatter(label_cbrt)
    cb.update_ticks()

    return cb
