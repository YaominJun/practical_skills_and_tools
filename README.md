# practical_skills_and_tools
the repo contains many practical skills including load CSV files, draw beautiful paper pictures and so on. Also, it includes many useful tools in Ubuntu and Windows!!!

## 1. load csv files and write data into csv files
(1) cpp</br>
[]()[C++: load csv files and write data into csv files](https://github.com/YaominJun/practical_skills_and_tools/tree/main/practical_skills/load_data_csv/cpp)
</br>
(2) matlab</br>
load csv files:

    path_data =  'XXXpath\result0.csv';
    data = csvread(path_data, 1);
</br>
write data to csv files: </br>

    csvwrite('XXXpath\xxx.csv', matrix);
</br>
(3) python</br>

    import pandas as pd  
    result0 = pd.read_csv("XXXpath\\result0.csv")

## 2.draw beautiful paper pictures: Gradient color map

## 3.ROS Rviz visualization skill
[]()[ROS rviz_visualization_tool](https://github.com/YaominJun/practical_skills_and_tools/tree/main/Ubuntu_tools/ROS/Rviz_visualization)

results:
![]()![](images/2020-11-23%2012-09-27屏幕截图.png)

2D cubes and 3D points: </br>
![]()![](images/2020-11-23%2012-08-22屏幕截图.png)
