qe=int(input(""))
if qe>1:
    for i in range(2,qe):
        if (qe % i) == 0:
            print("no")
            break
    else:
        print("yes")

else:
    print("no")
