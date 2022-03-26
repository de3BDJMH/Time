def m7(h1,m1,s1,h2,m2,s2):
    if h1<h2:
        h1,h2=h2,h1
        m1,m2=m2,m1
        s1,s2=s2,s1
    elif h1==h2:
        if m1<m2:
            h1,h2=h2,h1
            m1,m2=m2,m1
            s1,s2=s2,s1
        elif m1==m2:
            return [abs(s1-s2),(0,0,abs(s1-s2))]
    s=0
    if h1==h2:
        while m1!=m2:
            s=s+s1
            m1=m1-1
            s1=60
        s=s+s1
    else:
        while h1!=h2:
            while m1!=0:
                s=s+s1
                m1=m1-1
                s1=60
            h1=h1-1
            m1=60
        while m1!=m2:
            s=s+s1
            m1=m1-1
            s1=60
        s=s+(s1-s2)
    n=s
    h=s//60//60
    m=s//60%60
    s=s%60%60
    return [n,(h,m,s)]