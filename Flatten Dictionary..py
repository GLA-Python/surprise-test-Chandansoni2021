n = int(input())
n = n-1
print("1")
if(n>0):
    print("1 1")
    n = n-1
if(n>0):
    print("2 1")
    n = n-1
f  = 1
for i in range(1,n+1):
    print("1 ",end = "")
    if(f<=1):
        print("2 "*i,end = "")
        print("1 "*i,end = "")
        f = f+1
        if(f>3):
            f  = 0
    else:
        print("1 "*i,end ="")
        print("2 "*i,end = "")
        f = f+1
        if(f>3):
            f = 0
    print("1")















