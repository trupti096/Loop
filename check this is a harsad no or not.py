num=int(input("enter a number:- "))
i=num
s=0
while i>0:
	r=i%10
	s=s+r
	i=i//10
if num%s==0:
	print("it is harsad number")
else:
	print("it is not harsad number")