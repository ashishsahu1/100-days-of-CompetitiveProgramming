lst=[]
for _ in range(int(input())):
    lst = [int(x) for x in input()]
    print(lst[0]+lst[len(lst)-1])