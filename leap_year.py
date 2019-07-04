vq=int(input())
if(vq%4==0 or vq%400==0 and vq%100==0):
	print("yes")
else:
	print("no")
