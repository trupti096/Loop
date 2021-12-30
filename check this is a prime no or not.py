num=int(input("enter a number="))
i=1
factor=0
while i<=num:
	if num%i==0 and num%num==0:
		factor=factor+1
	i=i+1
if factor==2:
	    print(num,"it is a prime number")
else :
		print(num,"it is not a prime number")    