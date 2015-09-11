'''
Created on 12 Sep 2015

@author: mahi
'''

from tkinter import *

#create a root
root = Tk()
root.geometry("600x500+10+10")

#create a frame
myContainer = Frame(root)
myContainer.pack(side=TOP,expand=YES, fill=BOTH)

def button_click():
    print("Hello -  Welcome to Tkinter")


# Add a button to click
btn = Button(root, text="Push Me!", command=button_click)
btn.pack(side=TOP,  expand=YES)

root.mainloop()