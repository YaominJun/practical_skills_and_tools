# MATLAB的画图技巧

## scatter
其中，前两个是点坐标，第三个是点的尺寸size，`'gs'`是颜色(绿色)和形状(方形)，`'filled'`是填充点，`'LineWidth',0.5`是线宽尺寸，`'MarkerFaceColor', 'g'`是填充颜色。

    scatter(xStart，yStart, 120, 'gs','filled','LineWidth',0.5, 'MarkerFaceColor', 'g');