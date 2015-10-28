# coding= utf-8
from os.path import exists
import time

def main():
    init_file(Filename)
    reading(Filename)
    
    diary = []
    line = "~"
    while len(line) != 0:  
        line = raw_input(">")
        if line in help:
            print '''\
                  (๑•́ ₃ •̀๑)~需要帮助? 很简单喔~
                  输入完一行回车, 日记就保存了, 下次进来就看到了~
                  '''
        elif line in quit:
            break
        else: 
            diary.append('\n' + line) 
    save(Filename, diary)


def save(filename, diarys):
    localtime = []
    localtime.append('\n' + time.strftime("%F , D%w , %X")) 
    export = open(filename, 'a')
    export.writelines(localtime + diarys)
    export.close()
    
def reading(filename):
    with open(filename) as readbook: 
        for i in readbook:
            print i
    
def init_file(filename):
    if not exists(filename):
        f = open(filename, 'w')
        f.close()

if __name__=='__main__':
    Filename = "daily.txt"
    help = ['help', 'h', '?']
    quit = ['quit', 'q', 'Q', 'exit']
    main()
