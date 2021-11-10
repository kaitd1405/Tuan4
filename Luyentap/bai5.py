s = input()
ans = 0
for i in range(len(s)):
    for j in range(i):
        if (s.count(s[j:i])>=2) :
            ans=max(ans,i-j+1)
print(ans)