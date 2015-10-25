# coding=utf-8
from Tkinter import *

class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def callback(self, event):
        text = self.e.get()
        self.e.delete(0, END)
        self.t.insert(END, '\n'+text.encode('utf-8'))
        f = open("daily.log", 'a+')
        f.write('\n'+text.encode('utf-8'))
        f.close()

    def createWidgets(self):
        
        self.e = Entry(self, width=50)
        self.e.pack()
        self.e.bind('<Key-Return>', self.callback)

        self.t = Text(self)
        self.t.pack()
        f = open('daily.log').readlines()
        for i in f:
            # 1.0 文件内容倒着呈现 
            self.t.insert(END, i) 

        self.q = Button(self, text="退出", command=self.quit)
        self.q.pack()      

def main():
    root = Tk()
    root.title("每日笔记")
    MyDailyTK = App(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()
