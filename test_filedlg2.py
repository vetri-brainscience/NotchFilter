#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 07:38:10 2018

@author: vetri
"""

from  tkinter import *
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/home/vetri/Desktop/",title = "choose your file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
root.withdraw()