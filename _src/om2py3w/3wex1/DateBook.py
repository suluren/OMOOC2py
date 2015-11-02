# coding= utf-8
from os.path import exists
import time

def main():
    lines = []
    while True:  
        l = raw_input(">")
        if l in ['help', 'h', '?']:
            print '''\
                  (๑•́ ₃ •̀๑)~需要帮助? 很简单喔~
                  输入完一行回车, 日记就保存了, 下次进来就看到了~
                  '''
        elif l in ['quit', 'q', 'exit']:
            break
        else:
            lines.append('\n' + l)
    save(Filename, line)


def save(filename, line):
    diary = []
    diary.append('\n' + time.strftime("%F,D%w,%X") + ': ' + line) 
    export = open(filename, 'a+')
    export.writelines(diary)
    export.close()
    
def reading(filename):
    with open(filename) as readbook: 
        #for i in readbook:
            #print i
        return readbook.read()

 
def init_file(filename):
    if not exists(filename):
        f = open(filename, 'w')
        f.close()


if __name__=='__main__':
    Filename = "daily.log"
    init_file(Filename)
    print reading(Filename)   
    main()
