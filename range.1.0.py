#RANGE
range(5) #(0, 1, 2, 3, 4)
range(1, 5) #(1, 2, 3 ,4)
range(1, 6, 2) #(1, 3, 5)



import random
for i in range(6):
	n = random.randint(1, 2000)
	print(n)
	print('This is the', i+1, 'time random numbers are generated')