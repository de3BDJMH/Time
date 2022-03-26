def m9(h1,m1,s1,h2,m2,s2):
    h=h1+h2
    m=m1+m2
    s=s1+s2
    d=0
    while s>=60:
        s-=60
        m+=1
    while m>=60:
        h+=1
    while h>=24:
        h=h-24
        d=d+1
    return ((h,m,s),d)
def m9s(h1,m1,s1,s):
    h2=s//60//60
    m2=s//60%60
    s2=s%60%60
    return m9(h1,m1,s1,h2,m2,s2)