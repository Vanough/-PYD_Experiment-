# -*- coding: utf-8 -*-一款在方案初步简易计算楼梯的神器，输入开间，净深，净高后得出梯段宽度和休息平台宽度
"""
Created on Fri Nov 12 01:08:05 2021

@author: PUFFER
"""

print("————————————————楼梯计算神器———————————————— design by PUFFER ")
breadth = 1000 ('开间') #输入开间值
depth = 9000('进深')#输入进深值
clear_hight = 6000('净高')#输入净高值
wide,ladder_well,platform,ladder,tread= ('梯段宽度550*n','梯井','休息平台宽度','踢面','踏面')#定义楼梯变量
step = ('踏步数')#定义踏步数
int_clear_hight = int(clear_hight)#转化字符串为整数
int_breadth = int(breadth)#转化字符串为整数
int_depth = int(depth)#转化字符串为整数
if (int_clear_hight >25 (175*4)):
    step=int_clear_hight/175#计算踏步数量
    int_step = int(step)#取整
    ladder = int_clear_hight/int_step#计算踏面
    tread = 600-2*ladder#计算踢面
    wide = (int_breadth-1100)/2#计算梯段平台
    platform = (int_depth-(int_step-1)*ladder)/2#计算休息平台
    int_ladder = int (ladder)#浮点数转化为整数
    int_tread = int (tread)#浮点数转化为整数
    int_wide = int (wide)#浮点数转化为整数
    int_platform= int (platform)#浮点数转化为整数
    print('梯段宽度{}mm'.format(int_wide),'休息平台宽度{}mm'.format(int_platform),'踢面{}mm'.format(int_ladder),'踏面{}mm'.format(int_tread))#输出
else:
    print('错误')
