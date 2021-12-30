#           1  
#        2  2  2
#     3  3  3  3  3
#  4  4  4  4  4  4  4
#5  5  5  5  5  5  5  5  5
i=1
k=1
while i<=5:
	b=1
	while b<=5-i:
		print('',end=" ")
		b=b+1
	j=1
	while j<=k:
		print(i,end=" ")
		j=j+1
	k=k+2
	print()
	i=i+1