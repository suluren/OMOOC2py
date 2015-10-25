# coding=utf-8
from Tkinter import *
import ScrolledText as ST 
from os.path import exists
from random import choice

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def callback(self, event):
        text = self.e.get()
        self.e.delete(0, END)
        self.t.insert(END, '\n'+text.encode('utf-8'))
        f = open(filename, 'a+')
        f.write('\n'+text.encode('utf-8'))
        f.close()

    def createWidgets(self):
        v = StringVar()
        self.l = Label(self, textvariable=v)
        v.set(choice(emoji))
        self.l.pack()
        
        self.e = Entry(self, width=50)
        self.e.pack()
        self.e.bind('<Key-Return>', self.callback)

        self.t = ST.ScrolledText(self)
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
    filename =  "daily.log"
    if not exists(filename):
        f = open(filename, 'w')
        f.close()
    main()
