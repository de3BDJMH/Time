def m11(h,m,s):
    return h*3600+m*60+s
def m11s(s):
    return [s//60//60,s//60%60,s%60%60]