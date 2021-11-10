a = list(map(int,input().split()))
b = [i for i in range(len(a)) if a[i]%2==1]
a = [i for i in a if i%2==0]
print(a)
print(b)
