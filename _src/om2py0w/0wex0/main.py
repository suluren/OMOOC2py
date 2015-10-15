# -*- coding: UTF-8 -*-
# Quick Python Script Explanation for programmers
# 主食种类与食量建议，依据GL与GI值  

food_name = ['苹果', '大米', '燕麦']
GI_value = [36, 87, 55]
GI_list = zip(food_name, GI_value)
Dict = dict( (name,value) for name,value in GI_list)

def main():
	print '你好，我是小小A，将为你提供主食种类和食量建议，帮助你控制血糖~'
	print "推荐以下食材喔："
	
	list()
	opt = raw_input('\n请输入你选择的主食：')
	
	check(opt)
	
	quan = raw_input("\n次饭啦~小小A也饿了呢，你打算吃多少呢？以克计量哦~  ")
	
	GI = Dict.get(opt)
	gl = GI * int(quan) / 100
	
	advice(gl)
	
def list():
	for i in food_name:
		print i,
		
def check(opts):	
	if opts not in food_name:
		print "\n小小A伤脑筋呢~试试这些？" 
	else:
		return 
		
def advice(GL):
	if GL >= 20:
		print "噢哦……这可不是个好选择，再试试别的？"
	elif GL in range(10, 19):
		print "当主餐刚刚好哦，运动以后吃也不错~"
	elif GL in range(1, 9):
		print "当零食刚刚好哦，棒棒哒~"
	else:
		print "西北风吹呀吹~啊吹呀吹~~"
		
if __name__=='__main__':
	main()