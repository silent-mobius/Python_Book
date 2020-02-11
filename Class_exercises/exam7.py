import random

def ex6():
	count_up = 0 # 25
	count_down= 0 # 31
	total = 0 
	while total <=999:
		num = random.randint(10,99)
		total = total + num
		if num // 10 < num %10:
			count_up = count_up + 1
		elif num // 10 > num %10:
			count_down = count_down + 1
		
	print("total up number: ",str(count_up))
	print("total down number: ",str(count_down))


ex6()
