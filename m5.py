import month as mo
import m3
import m1
def m5(y,m,d,wd,wdn):
    w={"星期一":1,"星期二":2,"星期三":3,"星期四":4,"星期五":5,"星期六":6,"星期日":7}
    ymdwd=w[m3.m3(y,m,d)]
    if wd>=ymdwd:
        n=wdn*7+wd-7-ymdwd
    else:
        n=wdn*7+wd-ymdwd
    return m1.m1(y,m,d,n)