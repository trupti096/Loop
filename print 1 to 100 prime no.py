i=1
while i<=100:
	fac=0
	j=1
	while j<=i:
		if i%j==0:
			fac=fac+1
		j=j+1
	if fac==2:
		print(j,"prime no")
	else:
		print(j)
	i=i+1