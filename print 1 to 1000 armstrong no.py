i=1
while i<=1000:
	j=i
	sum=0
	while j>0:
		digit=j%10
		sum=sum+digit**len(str(i))
		j=j//10
	if i==sum:
		print(i,"Armstrong no")
	i=i+1