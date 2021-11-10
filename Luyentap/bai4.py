s = input()
a = "pangram"
cnt =0
for i in a:
    if (i in s.lower()):
        cnt+=1
if (cnt==7):
    print("YES")
else :
    print("NO")