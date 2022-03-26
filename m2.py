import month as mo
def m2(y1,m1,d1,y2,m2,d2):
    if y1>y2:
        y1,y2=y2,y1
        m1,m2=m2,m1
        d1,d2=d2,d1
    elif y1==y2:
        if m1>m2:
            y1,y2=y2,y1
            m1,m2=m2,m1
            d1,d2=d2,d1
        elif m1==m2:
            return abs(d1-d2)
    n=0
    if y1==y2:
        while m1!=m2:
            n+=d2
            m2=m2-1
            d2=mo.month(m2,y2)
        n=n+(mo.month(m1,y1)-d1)
        return n
    else:
        while y1!=y2:
            while m2!=1:
                n+=d2
                m2=m2-1
                d2=mo.month(m2,y2)
            n+=d2
            m2=12
            y2=y2-1
            d2=mo.month(m2,y2)
        while m2!=m1:
            n+=d2
            m2=m2-1
            d2=mo.month(m2,y2)
        n=n+(mo.month(m1,y1)-d1)
        return n