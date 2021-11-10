def count(n,a):
    cnt = {}
    for i in a :
        cnt[i]=0
    for i in a :
        cnt[i]+=1
    print(cnt)
n = int(input())
a = list(map(int,input().split()))
count(n,a)