s = input()
if (len(s)<2) :
    print("")
else :
    print(s[0:2:]+s[int(len(s)-2)::])