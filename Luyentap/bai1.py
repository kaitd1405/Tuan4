
s = input()
a = []
for i in range(len(s)):
    if (s[i]=='(' or s[i]==',' or s[i]== ')'):
        a.append(i)
print(s[a[0]+1:a[1]:],s[a[1]+1:a[2]:]) 