# coding=utf-8
from Tkinter import *
# from wr import writing

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        text = Text(frame)
        text.pack(side=LEFT) 

        q = Button(frame, text="退出", command=frame.quit)
        q.pack(side=BOTTOM)

        w = Button(frame, text="保存")
        w.pack(side=TOP)

        r = Button(frame, text="查看")
        r.pack(side=TOP)

root = Tk()
root.title("日记")
MyDailyTK = App(root)

root.mainloop()
