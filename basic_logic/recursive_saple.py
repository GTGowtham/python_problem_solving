def recurse(num):
    if num==1:
        return 1
    else:
        return num+recurse(num-1)
n=int(input())
recurse(n)