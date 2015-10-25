# coding=utf-8

from Tkinter import *


class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def callback(self):
        f = open("daily.log", 'a+')
        text = self.e.get()
        print text
        self.e.delete(0, END)
        f.write('\n' + text.encode('utf-8'))
        f.close()

    def createWidgets(self):
        
        self.e = Entry(self, width=50)
        self.e.pack()

        self.b = Button(self, text="保存", command=self.callback)
        self.b.pack()

        self.t = Text(self)
        self.t.pack() 

        self.q = Button(self, text="退出", command=self.quit)
        self.q.pack()      

def main():
    root = Tk()
    root.title("每日笔记")
    MyDailyTK = App(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()
