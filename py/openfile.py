# _*_ coding:utf-8 _*_
from tkinter import *
import re
import os
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog, StringVar


# 定义打开文件函数
def open_files():
    f_name = tkinter.filedialog.askopenfilenames(title='Open Files',            # 打开文件
                                                 filetypes=[('All Files', '*'), ('text file', '*.txt')])
    return f_name

open_files()
