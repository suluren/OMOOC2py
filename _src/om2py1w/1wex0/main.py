# -*- coding: UTF-8 -*-
from os.path import exists
import time

def main():
    if exists("datebook.txt") == True:
        reading()
        writing()    
    else:
        init_file = open('datebook.txt', 'w')
        init_file.write("hello~")
        init_file.close()
        
        writing()

def writing():
    diary = []
    localtime = time.strftime("%Y-%m-%d %X")

    line = "test"
    while len(line) != 0:  
        line = raw_input("> ")  
        diary.append(line + '\t' + localtime + '\n')

    export = open('datebook.txt', 'a+')
    export.writelines(diary)
    export.close()
    
def reading():
    diary = []
    readbook = open('datebook.txt')
    print readbook.read()

if __name__=='__main__':
	main()
           
            