def my_func(lst):
    s = []
    for i in range(0,(len(lst))-1):
        j = lst[i+1]-lst[i]
        s.append(abs(j))
    if sorted(set(s))==s:
        return True
    else:
        return False   
    print(sorted(s))
lst = list(map(int,input().split()))
out = my_func(lst)
print(out)

