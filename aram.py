n=int(input("enter a number:\n"))
sum=0
temp=n
while(temp>0):
	digit=temp%10
	sum+=digit**3
	temp=temp//10
if(n==sum):
	print(n,"is a Aramstrong number")
else:
	print(n,"is not a Aramstrong number")
