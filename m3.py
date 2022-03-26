import month as mo
import m2
def m3(y,m,d):
    w={1:"星期一",2:"星期二",3:"星期三",4:"星期四",5:"星期五",6:"星期六",7:"星期日"}
    n=m2.m2(2022,3,1,y,m,d)
    big=True
    if y>2022:
        big=True
    elif y==2022:
        if m>=3:
            big=True
        else:
            big=False
    else:
        big=False
    if big:
        wd=n%7+2
    else:
        wd=(8-n%7)%7+1
    return w[wd]