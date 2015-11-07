# coding= utf-8
from os.path import exists
import time
#import pickle

def main():
    lines = []
    while True:  
        line = raw_input(">")
        if line in ['help', 'h', '?']:
            print '''\
                  (๑•́ ₃ •̀๑)~需要帮助? 很简单喔~
                  输入完一行回车, 日记就保存了, 下次进来就看到了~
                  '''
        elif line in ['quit', 'q', 'exit']:
            break
        else:
            lines.append('\n' + line)
    saving(Filename, lines)


def saving(filename, data):
    diary = {time.strftime("%F,D%w,%X") : data} 
    f = open(filename, 'a+')
    #pickle.dump(diary, f)保存为 str; 越写越长orz...
    for schedule, valuelist in diary.items():
        f.write("\n%s" % schedule)
        for content in valuelist:
            f.write("%s" % content.encode('utf-8'))               
    f.close()
    
def reading(filename):
    with open(filename) as readbook:
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
