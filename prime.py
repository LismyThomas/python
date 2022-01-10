n=int(input("enter the input:"))
if(n>1):
	c=0
	for i in range(2,n):
		if(n%i==0):
			c=c+1
			break
		else:
			continue
	if(c==1):
		print("not prime")
	else:
		print("prime")