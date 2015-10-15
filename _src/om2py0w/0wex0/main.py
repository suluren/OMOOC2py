# -*- coding: UTF-8 -*-
# Quick Python Script Explanation for programmers
# 给程序员的超快py脚本解说
import os

def main():
	print 'Hello world!'
	
	print "this is Alice's greeting."
	print 'This is Bob\'s greeting.'
	
	foo(5, 10)
	
	print '=' * 10
	print 'Current working directory is '+os.getcwd()
	
	counter = 0
	counter += 1
	
	food = ('苹果', '杏子', '李子', '梨')
	for i in food:
		print '俺就爱整只'+i
		
	print '数到10'
	for i in range(10):
		print i,
		
def foo(param1, secondParam):
	res = param1+secondParam
	print '%s 加 %s 等于 %s'%(param1, secondParam, res)
	if res < 50:
		print '这个'
	elif (res>=50) and ((param1==42) or (secondParam==24)):
		print '那个'
	else:
		print '嗯...'
	return res # 这是单行注释
	'''这是多
行注释......'''

if __name__=='__main__':
	main()