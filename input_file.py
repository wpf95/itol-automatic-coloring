# _*_ coding: utf-8 _*_
"""
Created on 2023/9/14 10:38

@author: Wangpf

@Email: 206462763@qq.com
"""

from auto_color import select_number

fo = open(r'C:\Users\Desktop\itol_template.txt','r') #itol着色模板文件
f1 = open(r'C:\Users\Desktop\sample.txt','r') #个体信息文件
f2 = open(r'C:\Users\Desktop\sample.txt','r') #同上，same file
out = open(r"C:\Users\Desktop\itol_color.txt","w") #output文件，使用此文件拖拽至itol面板 着色
fo_line = 1
for line in fo:
    if fo_line >= 1 and fo_line <= 61:
        out.write(line)
    fo_line += 1

all_region=[]
for line in f1:
    line = line.strip().split()
    region = line[0]
    vcf_name = line[1]
    all_region.append(region)
region_list=list(set(all_region))
color_list = select_number(len(region_list))

for line in f2:
    line = line.strip().split()
    vcf_name = line[1]
    region = line[0]
    reco_index = region_list.index(region)
    color = color_list[reco_index]
    out.write(vcf_name+"\t"+"branch"+"\t"+color+"\t"+"normal"+"\n")
