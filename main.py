# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:32 2019

@author: 12107
"""

import win32api, win32con, win32gui
import numpy as np
import os

def set_wallpaper(img_path):
    # 打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)

def get_image_path(root_path=r'C:\Users\12107\Pictures\guidao'):
    file_list=os.listdir(root_path)
    rd=np.random.randint(0,len(file_list))
    img_path=root_path+'\\'+file_list[rd]
    return img_path

if __name__=='__main__':
    img_path=get_image_path()
    set_wallpaper(img_path)
    