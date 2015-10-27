# coding=utf-8
# author : suluren

from Tkinter import *
from ttk import *
import ScrolledText as ST 
from os.path import exists
from random import choice
# from DateBook import init_file

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def callback(self, event):
        text = self.e.get()
        self.e.delete(0, END)
        self.t.insert(END, '\n'+text.encode('utf-8'))
        f = open(filename, 'a')
        f.write('\n'+text.encode('utf-8'))
        f.close()

    def createWidgets(self):
        
        #v = StringVar()
        self.l = Label(self, text=choice(emoji))
        #v.set(choice(emoji))
        self.l.pack()
        
        c = StringVar()
        self.e = Entry(self, textvariable=c, width=50)
        #:ttk 下不能显示
        c.set("请在这里输入")
        self.e.pack()
        self.e.bind('<Key-Return>', self.callback)

        self.t = ST.ScrolledText(self, width=66)
        self.t.pack()
        f = open(filename).readlines()
        for i in f:
            self.t.insert(END, i) 

        self.q = Button(self, text="退出", command=self.quit)
        self.q.pack()      

def main():
    root = Tk()
    root.title("~每日笔记~")
    MyDailyTK = App(master=root)
    root.mainloop()

if __name__ == '__main__':
    emoji = ['ε٩(๑> ₃ <)۶з', '(¦3[▓▓]', 'ξ( ✿＞◡❛)', '(´ΘωΘ`)']
    filename = "daily.txt"
    #~ init_file(filename)
    if not exists(filename):
        f = open(filename, 'w')
        f.close()
    main()
