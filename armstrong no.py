num=int(input("enter a number: "))
i=num
s=0
while num>0:
	s=s+(num%10)(num%10)(num%10)
	num=num//10
if i==s:
	print("number is armstrong")
else:
	print("number is not armstrong")