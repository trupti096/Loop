num=int(input("enter a number="))
sum=0
x=num
while num>0:
	i=1
	fac=1
	rem=num%10
	while i<=rem:
		fac=fac*i
		i=i+1
	sum=sum+fac		
	num=num//10
if sum==x:
	print("strong no")
else:
	print("not a strong no")