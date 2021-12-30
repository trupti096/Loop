num=int(input("enter a number: "))
s=0
x=num
while num>0:
	s=(s*10)+num%10
	num=num//10
if x==s:
	print("palindrom number")
else:
	print("not a palindrom number")