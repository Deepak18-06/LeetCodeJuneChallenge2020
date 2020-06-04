s= ['h','e','l','l','o']
#print(s[::-1])
#s.reverse()
l = 0
r = len(s)-1
    while l<r:
        s[l],s[r] = s[r],s[l]
            l+=1
            r-=1