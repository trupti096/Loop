i=1
sum=0
sum2=0
count=0
count2=0
while i<=10:
	if i%2==0:
		sum=sum+i
		count=count+1
	else:
		sum2=sum2+i
		count2=count2+1
	i+=1
print("even",count)
print("odd",count2)
print("even",sum)
print("odd",sum2)
print("even",sum/count)
print("odd",sum2/count2)
