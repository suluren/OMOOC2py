# coding=utf-8
# author : suluren

from Tkinter import *
from ttk import *
#import ScrolledText as ST 
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
        
        self.c = StringVar()
        self.c.set("唷~~心情如何, 准备写点什么?(*ˇωˇ*人)在这里记录下吧...")
        self.e = Entry(self, textvariable=self.c, width=50)
        self.e.pack()
        self.e.bind('<Key-Return>', self.callback)

        self.sb = Scrollbar(self, orient=VERTICAL)
        self.t = Text(self, width=66, yscrollcommand=self.sb.set)
        self.sb.config(command=self.t.yview)
        self.sb.pack(side=RIGHT , fill=Y)
        self.t.pack()
        f = open(filename).readlines()
        for i in f:
            self.t.insert(END, i)  

        self.q = Button(self, text="退出", command=self.quit)
        self.q.pack()      

def main():
    root = Tk()
    root.title("~每日笔记~")
    #root.geometry("540x480")
    MyDailyTK = App(master=root)
    root.mainloop()

if __name__ == '__main__':
    emoji = ['ε٩(๑> ₃ <)۶з', '(¦3[▓▓]', 'ξ( ✿＞◡❛)', '(´ΘωΘ`)']
    filename = "daily.log"
    #~ init_file(filename)
    if not exists(filename):
        f = open(filename, 'w')
        f.close()
    main()
