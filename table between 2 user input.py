num=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
while num<=num2:
		j=1
		while j<=10:
			print(num,"×",j,"=",num*j)
			j+=1
		num+=1
		print(" ")