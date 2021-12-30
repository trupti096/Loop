i=1
count=0
while i<=100:
	j=i
	sum=0
	while j>0:
		r=j%10
		sum=sum+r
		j=j//10
	if i%sum==0:
		print(i,"harsad no")
		count=count+1
	else:
		print(i)
	i=i+1
print(count)