# _*_ coding: utf-8 _*_
"""
Created on 2023/9/14 9:32

@author: Wangpf

@Email: 206462763@qq.com
"""

import random
def select_number(times):
    color = open(r'C:\Users\Desktop\color.txt', encoding='gb18030', errors='ignore')
    color_set = []
    white_color = ["top","#ffffff","#f5f5f5","#000000","#fffaf0","#fffff0","#fff8dc","#faf0e6","#fff5ee","#fffafa","#f5fffa","#f0fff0","#f0ffff","#f0f8ff","#f8f8ff","#fff0f5"]
    for line in color:
        if "bgcolor" in line :
            color = line.split('"')[1]
            if color in white_color :
                pass
            else:
                color_set.append(color)
    start = random.randint(1,5)
    random_edge = (len(color_set)-start)//times
    index = []
    for i in range(int(times)):
        index.append(start)
        start=start+random.randint(5,random_edge)
    color_list=[]
    for i in index:
        color_list.append(color_set[i])
    return color_list






