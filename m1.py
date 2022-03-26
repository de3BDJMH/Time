import month as mo
def m1(year,month,day,n):
    while n>=0:
        m_d=mo.month(month,year)
        n=n-(m_d-day)
        if n>0:
            month=month+1
            if month>12:
                year=year+1
                month=1
        day=0
    while n<=0:
        n=n+mo.month(month,year)
    day=n
    return year,month,day