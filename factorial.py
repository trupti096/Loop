n=int(input("enter a no="))
fac=1
sum=0
while n>0:
	if n==0 and n==1:
		sum=sum+fac
	else:
		fac=fac*n
	n=n-1
print(fac)