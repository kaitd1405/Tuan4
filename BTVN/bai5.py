def Find(x,a):
    for i in range(len(a)):
        if (a[i]==x) :
            print(i)
            del a[i]
            print(a)
            break;
def Findall(x,a):
    a = [i for i in a if i!=x]
    print(a)
def Chen(x,y,a):
    a.insert(y,x)
    print(a)
x = int(input())
a = list(map(int,input().split()))
Find(x,a)
Findall(x,a)
y = int(input())
Chen(x,y,a)