qw=input("")
qw=qw.casefold()
rev=reversed(qw)
if list(qw) == list(rev):
	print("yes")
else:
	print("no")
