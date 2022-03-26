import month as mo
import m2
def m4(y1,mo1,d1,y2,mo2,d2,wd):
    n=m2.m2(y1,mo1,d1,y2,mo2,d2)
    weekday=n%7+2
    week=n//7
    if 2<weekday:
        if 2<=wd<=weekday:
            return week+1
        else:
            return week
    else:
        if weekday<=wd<=2:
            return week+1
        else:
            return week