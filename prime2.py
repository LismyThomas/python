low=int(input("enter LOWER RANGE:"))
high=int(input("enter HIGHER RANGE:"))
for num in range(low,high+1):
	if(num>1):
		for i in range(2,num):
			if(num%i==0):
				break
		else:
			print(num)