# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:58:51 2022

@author: INDHRNA
"""

import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, filedialog

import wolframalpha
import threading



#%%%


class Pybot:
    def __init__(self,root):
        self.root = root
        self.font = ('arial',12)
        self.background_color = '#7e7a79'
        self.text_color = '#ffffff'
        
if __name__ == '__main__':
    root =Tk()
    root.title('Pybot - Indhra')
    root.geometry('500x520')
    root.config(bg='#403b3a')
    root.resizable(0,0)
    Pybot(root)
    root.mainloop()
