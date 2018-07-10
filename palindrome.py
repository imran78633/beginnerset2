a=121
num=a
rev=0
while(a>0):
	rem=a%10
	a=a/10
	rev=rev*10+rem
if (num==rev):
	print ('yes')
else:
	print ('no')
