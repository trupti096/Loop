#         5
#       4 4
#     3 3 3
#   2 2 2 2
# 1 1 1 1 1
i=1
while i<=5:
	b=1
	while b<=5-i:
		print('  ',end="")
		b=b+1
	j=1
	while j<=i:
		print(b,end=" ")
		j=j+1
	print( )
	i=i+1