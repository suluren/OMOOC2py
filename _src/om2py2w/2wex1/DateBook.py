# coding= utf-8
from os.path import exists
import time

def main():
    init_file()
    reading()
    writing()    

def writing():
    diary = []
    localtime = []
    line = "~"
    
    while len(line) != 0:  
        line = raw_input(">")
        if line in help:
            print "(๑•́ ₃ •̀๑)~需要帮助? 很简单喔~\
                  输入完一行回车, 日记就保存了, 下次进来就看到了~" 
        else: 
            diary.append(line + '\n')

    localtime.append(time.strftime("%F , *wd%w , %X") + '\n') 
    export = open(filename, 'a')
    export.writelines(diary + localtime)
    export.close()
    
def reading():
    readbook = open(filename).readlines()
    for i in readbook:
        print i
    readbook.close()

def init_file(filename):
    if not exists(filename):
        f = open(filename, 'w')
        f.close()

if __name__=='__main__':
    filename = "datebook.txt"
    help = ['help', 'h', '?']
    main()
