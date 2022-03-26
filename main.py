import month as mo
import playsound
import m1
import m2
import m3
import m4
import m5
import m6
import m7
import m8
import m9
import m10
import m11
import m12
import m13

import tkinter as tk
from tkinter import ttk
import random
import datetime
import time

class App(ttk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self)
        self.v=tk.IntVar(window)
        self.del_image=tk.PhotoImage(file="delete.png")
        self.screen()
        self.table_info={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0}
        self.table=None
        self.table_list=[]
        self.trick=0

    def screen(self):
        raidiobutton_style1=ttk.Style(window)
        raidiobutton_style1.configure("fontstyle1.TRadiobutton",font=("等线",15))
        raidiobutton_style2=ttk.Style(window)
        raidiobutton_style2.configure("fontstyle2.TRadiobutton",font=("等线",15,"bold"),foreground="red")
        self.l=ttk.Label(window,text="选择模式",font=("等线",16,"bold"),foreground="#660099")
        self.radiobuttom=ttk.Labelframe(self,padding=(10,10),labelwidget=self.l)
        self.radiobuttom.grid(column=0,row=0,padx=(20,10), pady=20,sticky="nsew")
        self.scrollbar1=ttk.Scrollbar(self.radiobuttom,orient="vertical")
        self.scrollbar2=ttk.Scrollbar(self.radiobuttom,orient="horizontal")
        
        self.c=tk.Canvas(self.radiobuttom,yscrollcommand=self.scrollbar1.set,width=250,height=490,xscrollcommand=self.scrollbar2.set,highlightthickness=0)
        self.frame=ttk.Frame(self.c)
        self.c.create_window(0,0,window=self.frame,anchor="nw")
        self.scrollbar1.configure(command=self.c.yview)
        self.scrollbar1.grid(column=1,row=0,sticky="ns")
        self.scrollbar2.configure(command=self.c.xview)
        self.scrollbar2.grid(column=0,row=1,sticky="ew")
        self.c.grid(column=0,row=0)

        self.f1=ttk.Frame(self,padding=(10,25))
        self.f1.grid(column=1,row=0,sticky="nsew")
        self.note=ttk.Notebook(self.f1,width=550,height=510)
        self.note.grid(column=1,row=0,sticky="nsew")

        self.l1=ttk.Radiobutton(self.frame,text="1.几天后的日期",variable=self.v,value=1,style="fontstyle1.TRadiobutton")
        self.l1.bind("<Button-1>",func=self.mm1)
        self.l1.grid(column=0,row=1, padx=5, pady=10,sticky="nsew")
        self.l2=ttk.Radiobutton(self.frame,text="2.两个日期之间相隔的日数",variable=self.v,value=2,style="fontstyle1.TRadiobutton")
        self.l2.bind("<Button-1>",func=self.mm2)
        self.l2.grid(column=0,row=2, padx=5, pady=10,sticky="nsew")
        self.l3=ttk.Radiobutton(self.frame,text="3.查询某日是星期几",variable=self.v,value=3,style="fontstyle1.TRadiobutton")
        self.l3.bind("<Button-1>",func=self.mm3)
        self.l3.grid(column=0,row=3, padx=5, pady=10,sticky="nsew")
        self.l4=ttk.Radiobutton(self.frame,text="4.到某日之前有几个星期几",variable=self.v,value=4,style="fontstyle1.TRadiobutton")
        self.l4.bind("<Button-1>",func=self.mm4)
        self.l4.grid(column=0,row=4, padx=5, pady=10,sticky="nsew")
        self.l5=ttk.Radiobutton(self.frame,text="5.接下来第几个星期几是几日",variable=self.v,value=5,style="fontstyle1.TRadiobutton")
        self.l5.bind("<Button-1>",func=self.mm5)
        self.l5.grid(column=0,row=5, padx=5, pady=10,sticky="nsew")
        self.l6=ttk.Radiobutton(self.frame,text="6.农历查询",variable=self.v,value=6,style="fontstyle1.TRadiobutton")
        self.l6.bind("<Button-1>",func=self.mm6)
        self.l6.grid(column=0,row=6, padx=5, pady=10,sticky="nsew")
        self.l7=ttk.Radiobutton(self.frame,text="7.两个时间点相差几秒（分、时）",variable=self.v,value=7,style="fontstyle1.TRadiobutton")
        self.l7.bind("<Button-1>",func=self.mm7)
        self.l7.grid(column=0,row=7, padx=5, pady=10,sticky="nsew")
        self.l8=ttk.Radiobutton(self.frame,text="8.距离高考剩余时间",variable=self.v,value=8,style="fontstyle2.TRadiobutton")
        self.l8.bind("<Button-1>",func=self.mm8)
        self.l8.grid(column=0,row=8, padx=5, pady=10,sticky="nsew")
        self.l9=ttk.Radiobutton(self.frame,text="9.几秒（分、时）后的时刻",variable=self.v,value=9,style="fontstyle1.TRadiobutton")
        self.l9.bind("<Button-1>",func=self.mm9)
        self.l9.grid(column=0,row=9, padx=5, pady=10,sticky="nsew")
        self.l10=ttk.Radiobutton(self.frame,text="10.定点报时",variable=self.v,value=10,style="fontstyle1.TRadiobutton")
        self.l10.bind("<Button-1>",func=self.mm10)
        self.l10.grid(column=0,row=10, padx=5, pady=10,sticky="nsew")
        self.l11=ttk.Radiobutton(self.frame,text="11.时分秒和秒转换",variable=self.v,value=11,style="fontstyle1.TRadiobutton")
        self.l11.bind("<Button-1>",func=self.mm11)
        self.l11.grid(column=0,row=11, padx=5, pady=10,sticky="nsew")
        self.l12=ttk.Radiobutton(self.frame,text="12.秒表",variable=self.v,value=12,style="fontstyle1.TRadiobutton")
        self.l12.bind("<Button-1>",func=self.mm12)
        self.l12.grid(column=0,row=12, padx=5, pady=10,sticky="nsew")
        self.l13=ttk.Radiobutton(self.frame,text="13.倒计时",variable=self.v,value=12,style="fontstyle1.TRadiobutton")
        self.l13.bind("<Button-1>",func=self.mm13)
        self.l13.grid(column=0,row=13, padx=5, pady=10,sticky="nsew")
        
        window.update()
        self.c.config(scrollregion=self.c.bbox("all"))

    def db(self):
        def dt(event=None):
            t=self.table
            if self.table_list.index(self.table)+1<len(self.table_list):
                self.table=self.table_list[self.table_list.index(self.table)+1]
            elif self.table_list.index(self.table)-1>=0:
                self.table=self.table_list[self.table_list.index(self.table)-1]
            if t[1]!=8:
                t[0].destroy()
                self.table_info[t[1]]=0
                self.table_list.remove(t)
            else:
                def des(event=None):
                    warning.destroy()
                    self.table81.destroy()
                    self.table_info[8]=0
                    self.table_list.remove([self.table81,8])
                    self.trick=0
                    if sum(self.table_info.values())==0:
                        self.delbutton.destroy()
                def trick(event=None):
                    if self.trick<=10:
                        warning.place(x=self.note.winfo_width()/2-random.randint(0,250),y=self.note.winfo_height()/2-random.randint(0,150))
                        self.trick+=1
                    else:
                        des()
                warning=ttk.Label(self.note,text="你还想关掉??",font=("黑体",50),foreground="#C0C0C0")
                warning.place(x=self.note.winfo_width()/2-150,y=self.note.winfo_height()/2-80)
                warning.bind("<Enter>",func=trick)
            if sum(self.table_info.values())==0:
                self.delbutton.destroy()
                
        if sum(self.table_info.values())==1:
            self.delbutton=ttk.Button(self.note,image=self.del_image)
            self.delbutton.place(x=self.note.winfo_width()-100,y=self.note.winfo_height()-45)
            self.delbutton.bind("<Button-1>",func=dt)
        self.delbutton.lift()

    def mm1(self,event=None):
        def info_get(event):
            y=self.combobox11.get()
            m=self.combobox12.get()
            d=self.combobox13.get()
            n=self.combobox14.get()
            self.combobox13.configure(values=[i for i in range(1,mo.month(int(m),int(y))+1)])
            return y,m,d,n
        def mode1():
            y,m,d,n=info_get(None)
            year,month,day=m1.m1(int(y),int(m),int(d),int(n))
            self.label16.configure(text=f"{year}年{month}月{day}日")
        def tp(event):
            self.table=[self.table11,1]

        style1=ttk.Style()
        style1.configure("font.TButton",font=("等线",13,"bold"),foreground="#1E90FF")
        if self.table_info[1]<1:
            self.table_info[1]=1
            self.table11=ttk.Frame(self.note)
            self.table11.bind("<Enter>",func=tp)
            self.table_list.append([self.table11,1])
            self.note.add(self.table11,text="模式1")
            self.frame11=ttk.Frame(self.table11)
            self.frame11.grid(column=0,row=0,sticky="ew")
            self.combobox11=ttk.Combobox(self.frame11,values=[i for i in range(1900,2500)],width=10,font=("等线",11))
            self.combobox11.grid(column=0,row=0,padx=10,pady=15)
            self.combobox11.current(100)
            self.combobox11.bind("<Enter>",func=info_get)
            self.label11=ttk.Label(self.frame11,text="年",font=("等线",13))
            self.label11.grid(column=1,row=0,padx=5,pady=15)
            self.combobox12=ttk.Combobox(self.frame11,values=[i for i in range(1,13)],width=10,font=("等线",11))
            self.combobox12.grid(column=2,row=0,padx=5,pady=15)
            self.combobox12.current(0)
            self.combobox12.bind("<Enter>",func=info_get)
            self.label12=ttk.Label(self.frame11,text="月",font=("等线",13))
            self.label12.grid(column=3,row=0,padx=5,pady=15)
            self.combobox13=ttk.Combobox(self.frame11,values=[i+1 for i in range(mo.month(1,2020))],width=10,font=("等线",11))
            self.combobox13.grid(column=4,row=0,padx=5,pady=15)
            self.combobox13.current(0)
            self.combobox13.bind("<Enter>",func=info_get)
            self.label13=ttk.Label(self.frame11,text="日",font=("等线",13))
            self.label13.grid(column=5,row=0,padx=5,pady=15)
            self.frame12=ttk.Frame(self.table11)
            self.frame12.grid(column=0,row=1,sticky="ew")
            self.label14=ttk.Label(self.frame12,text="在",font=("等线",13))
            self.label14.grid(column=0,row=0,padx=10,pady=10)
            self.combobox14=ttk.Combobox(self.frame12,values=[i+1 for i in range(1000)],width=10,font=("等线",11))
            self.combobox14.grid(column=1,row=0,padx=5,pady=10)
            self.combobox14.current(0)
            self.combobox14.bind("<Enter>",func=info_get)
            self.label15=ttk.Label(self.frame12,text="天后是",font=("等线",13))
            self.label15.grid(column=2,row=0,padx=5,pady=10)
            y,m,d,n=info_get(None)
            year,month,day=m1.m1(int(y),int(m),int(d),int(n))
            self.label16=ttk.Label(self.frame12,text=f"{year}年{month}月{day}日",font=("等线",15,"bold"),foreground="#FFA500")
            self.label16.grid(column=3,row=0,padx=50,pady=10)
            self.button11=ttk.Button(self.frame12,text="点击进行计算",style="font.TButton",command=mode1)
            self.button11.grid(column=0,row=1,columnspan=2,padx=10,pady=20,ipadx=5,ipady=5)

            #self.delbutton1=ttk.Button(self.table11,image=self.del_image)
            #self.delbutton1.bind("<Button-1>",func=del_tab)
            #self.delbutton1.place(x=self.table11.winfo_width()-80,y=self.table11.winfo_height()-70)#想了1小时...
            self.db()

    def mm2(self,event):
        def info_get(event=None):
            y1=self.combobox21.get()
            m1=self.combobox22.get()
            d1=self.combobox23.get()
            self.combobox23.configure(values=[i for i in range(1,mo.month(int(m1),int(y1))+1)])
            y2=self.combobox24.get()
            m2=self.combobox25.get()
            d2=self.combobox26.get()
            self.combobox26.configure(values=[i for i in range(1,mo.month(int(m2),int(y2))+1)])
            return y1,m1,d1,y2,m2,d2
        def tp(event):
            self.table=[self.table21,2]
        def mode2(event=None):
            y1,mo1,d1,y2,mo2,d2=info_get()
            n=m2.m2(int(y1),int(mo1),int(d1),int(y2),int(mo2),int(d2))
            self.label28.configure(text=f"{n}")

        style2=ttk.Style()
        style2.configure("font.TButton",font=("等线",13,"bold"),foreground="#1E90FF")
        if self.table_info[2]<1:
            self.table_info[2]=1
            self.table21=ttk.Frame(self.note)
            self.table21.bind("<Enter>",func=tp)
            self.table_list.append([self.table21,2])
            self.note.add(self.table21,text="模式2")
            self.frame21=ttk.Frame(self.table21)
            self.frame21.grid(column=0,row=0,sticky="ew")
            self.combobox21=ttk.Combobox(self.frame21,values=[i for i in range(1900,2500)],width=10,font=("等线",11))
            self.combobox21.grid(column=0,row=0,padx=10,pady=15)
            self.combobox21.current(100)
            self.combobox21.bind("<Enter>",func=info_get)
            self.label21=ttk.Label(self.frame21,text="年",font=("等线",13))
            self.label21.grid(column=1,row=0,padx=5,pady=15)
            self.combobox22=ttk.Combobox(self.frame21,values=[i for i in range(1,13)],width=10,font=("等线",11))
            self.combobox22.grid(column=2,row=0,padx=5,pady=15)
            self.combobox22.current(0)
            self.combobox22.bind("<Enter>",func=info_get)
            self.label22=ttk.Label(self.frame21,text="月",font=("等线",13))
            self.label22.grid(column=3,row=0,padx=5,pady=15)
            self.combobox23=ttk.Combobox(self.frame21,values=[i+1 for i in range(mo.month(1,2020))],width=10,font=("等线",11))
            self.combobox23.grid(column=4,row=0,padx=5,pady=15)
            self.combobox23.current(0)
            self.combobox23.bind("<Enter>",func=info_get)
            self.label23=ttk.Label(self.frame21,text="日",font=("等线",13))
            self.label23.grid(column=5,row=0,padx=5,pady=15)
            self.frame22=ttk.Frame(self.table21)
            self.frame22.grid(column=0,row=1,sticky="ew")
            self.combobox24=ttk.Combobox(self.frame22,values=[i for i in range(1900,2500)],width=10,font=("等线",11))
            self.combobox24.grid(column=0,row=0,padx=10,pady=15)
            self.combobox24.current(100)
            self.combobox24.bind("<Enter>",func=info_get)
            self.label24=ttk.Label(self.frame22,text="年",font=("等线",13))
            self.label24.grid(column=1,row=0,padx=5,pady=15)
            self.combobox25=ttk.Combobox(self.frame22,values=[i for i in range(1,13)],width=10,font=("等线",11))
            self.combobox25.grid(column=2,row=0,padx=5,pady=15)
            self.combobox25.current(0)
            self.combobox25.bind("<Enter>",func=info_get)
            self.label25=ttk.Label(self.frame22,text="月",font=("等线",13))
            self.label25.grid(column=3,row=0,padx=5,pady=15)
            self.combobox26=ttk.Combobox(self.frame22,values=[i+1 for i in range(mo.month(1,2020))],width=10,font=("等线",11))
            self.combobox26.grid(column=4,row=0,padx=5,pady=15)
            self.combobox26.current(0)
            self.combobox26.bind("<Enter>",func=info_get)
            self.label26=ttk.Label(self.frame22,text="日",font=("等线",13))
            self.label26.grid(column=5,row=0,padx=5,pady=15)
            self.frame23=ttk.Frame(self.table21)
            self.frame23.grid(column=0,row=2,sticky="ew")
            self.label27=ttk.Label(self.frame23,text="之间相隔",font=("等线",13))
            self.label27.grid(column=0,row=0,padx=10,pady=15)
            self.label28=ttk.Label(self.frame23,text="0",font=("等线",17,"bold"),foreground="#FFA500")
            self.label28.grid(column=1,row=0,padx=20,pady=15)
            self.label29=ttk.Label(self.frame23,text="天",font=("等线",13))
            self.label29.grid(column=2,row=0,padx=20,pady=15)
            
            self.button21=ttk.Button(self.frame23,text="点击进行计算",style="font.TButton",command=mode2)
            self.button21.grid(column=0,row=1,columnspan=2,padx=10,pady=20,ipadx=5,ipady=5)

            self.db()

    def mm3(self,event=None):
        def info_get(event=None):
            y=self.combobox31.get()
            m=self.combobox32.get()
            d=self.combobox33.get()
            self.combobox33.configure(values=[i for i in range(1,mo.month(int(m),int(y))+1)])
            return y,m,d
        def mode3(event=None):
            y,m,d=info_get()
            n=m3.m3(int(y),int(m),int(d))
            self.label35.configure(text=n)
        def tp(event):
            self.table=[self.table31,3]

        style3=ttk.Style()
        style3.configure("font.TButton",font=("等线",13,"bold"),foreground="#1E90FF")
        if self.table_info[3]<1:
            self.table_info[3]=1
            self.table31=ttk.Frame(self.note)
            self.table31.bind("<Enter>",func=tp)
            self.table_list.append([self.table31,3])
            self.note.add(self.table31,text="模式3")
            self.frame31=ttk.Frame(self.table31)
            self.frame31.grid(column=0,row=0,sticky="ew")
            self.combobox31=ttk.Combobox(self.frame31,values=[i for i in range(1900,2500)],width=10,font=("等线",11))
            self.combobox31.grid(column=0,row=0,padx=10,pady=15)
            self.combobox31.current(100)
            self.combobox31.bind("<Enter>",func=info_get)
            self.label31=ttk.Label(self.frame31,text="年",font=("等线",13))
            self.label31.grid(column=1,row=0,padx=5,pady=15)
            self.combobox32=ttk.Combobox(self.frame31,values=[i for i in range(1,13)],width=10,font=("等线",11))
            self.combobox32.grid(column=2,row=0,padx=5,pady=15)
            self.combobox32.current(0)
            self.combobox32.bind("<Enter>",func=info_get)
            self.label32=ttk.Label(self.frame31,text="月",font=("等线",13))
            self.label32.grid(column=3,row=0,padx=5,pady=15)
            self.combobox33=ttk.Combobox(self.frame31,values=[i+1 for i in range(mo.month(1,2020))],width=10,font=("等线",11))
            self.combobox33.grid(column=4,row=0,padx=5,pady=15)
            self.combobox33.current(0)
            self.combobox33.bind("<Enter>",func=info_get)
            self.label33=ttk.Label(self.frame31,text="日",font=("等线",13))
            self.label33.grid(column=5,row=0,padx=5,pady=15)
            self.frame32=ttk.Frame(self.table31)
            self.frame32.grid(column=0,row=1,sticky="ew")
            self.label34=ttk.Label(self.frame32,text="是",font=("等线",13))
            self.label34.grid(column=0,row=0,padx=10,pady=15)
            self.label35=ttk.Label(self.frame32,text="",font=("等线",17,"bold"),foreground="#FFA500")
            self.label35.grid(column=1,row=0,padx=20,pady=15)

            self.button31=ttk.Button(self.frame32,text="点击进行计算",style="font.TButton",command=mode3)
            self.button31.grid(column=0,row=1,columnspan=2,padx=10,pady=20,ipadx=5,ipady=5)

            self.db()

    def mm4(self,event=None):
        def info_get(event=None):
            w={"星期一":1,"星期二":2,"星期三":3,"星期四":4,"星期五":5,"星期六":6,"星期日":7}
            y1=self.combobox41.get()
            m1=self.combobox42.get()
            d1=self.combobox43.get()
            self.combobox43.configure(values=[i for i in range(1,mo.month(int(m1),int(y1))+1)])
            y2=self.combobox44.get()
            m2=self.combobox45.get()
            d2=self.combobox46.get()
            self.combobox46.configure(values=[i for i in range(1,mo.month(int(m2),int(y2))+1)])
            wd=self.combobox47.get()
            return y1,m1,d1,y2,m2,d2,w[wd]
        def mode4(event=None):
            y1,mo1,d1,y2,mo2,d2,wd=info_get()
            n=m4.m4(int(y1),int(mo1),int(d1),int(y2),int(mo2),int(d2),int(wd))
            self.label48.configure(text=n)
        def tp(event):
            self.table=[self.table41,4]

        style4=ttk.Style()
        style4.configure("font.TButton",font=("等线",13,"bold"),foreground="#1E90FF")
        if self.table_info[4]<1:
            self.table_info[4]=1
            self.table41=ttk.Frame(self.note)
            self.table41.bind("<Enter>",func=tp)
            self.table_list.append([self.table41,4])
            self.note.add(self.table41,text="模式4")
            self.frame41=ttk.Frame(self.table41)
            self.frame41.grid(column=0,row=0,sticky="ew")
            self.combobox41=ttk.Combobox(self.frame41,values=[i for i in range(1900,2500)],width=10,font=("等线",11))
            self.combobox41.grid(column=0,row=0,padx=10,pady=15)
            self.combobox41.current(100)
            self.combobox41.bind("<Enter>",func=info_get)
            self.label41=ttk.Label(self.frame41,text="年",font=("等线",13))
            self.label41.grid(column=1,row=0,padx=5,pady=15)
            self.combobox42=ttk.Combobox(self.frame41,values=[i for i in range(1,13)],width=10,font=("等线",11))
            self.combobox42.grid(column=2,row=0,padx=5,pady=15)
            self.combobox42.current(0)
            self.combobox42.bind("<Enter>",func=info_get)
            self.label42=ttk.Label(self.frame41,text="月",font=("等线",13))
            self.label42.grid(column=3,row=0,padx=5,pady=15)
            self.combobox43=ttk.Combobox(self.frame41,values=[i+1 for i in range(mo.month(1,2020))],width=10,font=("等线",11))
            self.combobox43.grid(column=4,row=0,padx=5,pady=15)
            self.combobox43.current(0)
            self.combobox43.bind("<Enter>",func=info_get)
            self.label43=ttk.Label(self.frame41,text="日",font=("等线",13))
            self.label43.grid(column=5,row=0,padx=5,pady=15)
            self.frame42=ttk.Frame(self.table41)
            self.frame42.grid(column=0,row=1,sticky="ew")
            self.combobox44=ttk.Combobox(self.frame42,values=[i for i in range(1900,2500)],width=10,font=("等线",11))
            self.combobox44.grid(column=0,row=0,padx=10,pady=15)
            self.combobox44.current(100)
            self.combobox44.bind("<Enter>",func=info_get)
            self.label44=ttk.Label(self.frame42,text="年",font=("等线",13))
            self.label44.grid(column=1,row=0,padx=5,pady=15)
            self.combobox45=ttk.Combobox(self.frame42,values=[i for i in range(1,13)],width=10,font=("等线",11))
            self.combobox45.grid(column=2,row=0,padx=5,pady=15)
            self.combobox45.current(0)
            self.combobox45.bind("<Enter>",func=info_get)
            self.label45=ttk.Label(self.frame42,text="月",font=("等线",13))
            self.label45.grid(column=3,row=0,padx=5,pady=15)
            self.combobox46=ttk.Combobox(self.frame42,values=[i+1 for i in range(mo.month(1,2020))],width=10,font=("等线",11))
            self.combobox46.grid(column=4,row=0,padx=5,pady=15)
            self.combobox46.current(0)
            self.combobox46.bind("<Enter>",func=info_get)
            self.label46=ttk.Label(self.frame42,text="日",font=("等线",13))
            self.label46.grid(column=5,row=0,padx=5,pady=15)
            self.frame43=ttk.Frame(self.table41)
            self.frame43.grid(column=0,row=2,sticky="ew")
            self.label47=ttk.Label(self.frame43,text="之间相隔",font=("等线",13))
            self.label47.grid(column=0,row=0,padx=10,pady=15)
            self.label48=ttk.Label(self.frame43,text="",font=("等线",17,"bold"),foreground="#FFA500")
            self.label48.grid(column=1,row=0,padx=20,pady=15)
            self.label49=ttk.Label(self.frame43,text="个",font=("等线",13))
            self.label49.grid(column=2,row=0,padx=20,pady=15)
            self.combobox47=ttk.Combobox(self.frame43,values=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"],width=10,font=("等线",11))
            self.combobox47.grid(column=3,row=0,padx=5,pady=15)
            self.combobox47.current(0)
            self.combobox47.bind("<Enter>",func=info_get)
            
            self.button41=ttk.Button(self.frame43,text="点击进行计算",style="font.TButton",command=mode4)
            self.button41.grid(column=0,row=1,columnspan=2,padx=10,pady=20,ipadx=5,ipady=5)

            self.db()

    def mm5(self,event=None):
        def info_get(event=None):
            y=self.combobox51.get()
            m=self.combobox52.get()
            d=self.combobox53.get()
            self.combobox53.configure(values=[i for i in range(1,mo.month(int(m),int(y))+1)])
            wd=self.combobox55.get()
            wdn=self.combobox54.get()
            return y,m,d,wd,wdn
        def mode5(event=None):
            w={"星期一":1,"星期二":2,"星期三":3,"星期四":4,"星期五":5,"星期六":6,"星期日":7}
            y,m,d,wd,wdn=info_get()
            wd=w[wd]
            n=m5.m5(int(y),int(m),int(d),int(wd),int(wdn))
            self.label57.configure(text=f"{n[0]} 年 {n[1]} 月 {n[2]} 日")
        def tp(event):
            self.table=[self.table51,5]

        style5=ttk.Style()
        style5.configure("font.TButton",font=("等线",13,"bold"),foreground="#1E90FF")
        if self.table_info[5]<1:
            self.table_info[5]=1
            self.table51=ttk.Frame(self.note)
            self.table51.bind("<Enter>",func=tp)
            self.table_list.append([self.table51,5])
            self.note.add(self.table51,text="模式5")
            self.frame51=ttk.Frame(self.table51)
            self.frame51.grid(column=0,row=0,sticky="ew")
            self.combobox51=ttk.Combobox(self.frame51,values=[i for i in range(1900,2500)],width=10,font=("等线",11))
            self.combobox51.grid(column=0,row=0,padx=10,pady=15)
            self.combobox51.current(100)
            self.combobox51.bind("<Enter>",func=info_get)
            self.label51=ttk.Label(self.frame51,text="年",font=("等线",13))
            self.label51.grid(column=1,row=0,padx=5,pady=15)
            self.combobox52=ttk.Combobox(self.frame51,values=[i for i in range(1,13)],width=10,font=("等线",11))
            self.combobox52.grid(column=2,row=0,padx=5,pady=15)
            self.combobox52.current(0)
            self.combobox52.bind("<Enter>",func=info_get)
            self.label52=ttk.Label(self.frame51,text="月",font=("等线",13))
            self.label52.grid(column=3,row=0,padx=5,pady=15)
            self.combobox53=ttk.Combobox(self.frame51,values=[i+1 for i in range(mo.month(1,2020))],width=10,font=("等线",11))
            self.combobox53.grid(column=4,row=0,padx=5,pady=15)
            self.combobox53.current(0)
            self.combobox53.bind("<Enter>",func=info_get)
            self.label53=ttk.Label(self.frame51,text="日",font=("等线",13))
            self.label53.grid(column=5,row=0,padx=5,pady=15)
            self.frame52=ttk.Frame(self.table51)
            self.frame52.grid(column=0,row=1,sticky="ew")
            self.label54=ttk.Label(self.frame52,text="在",font=("等线",13))
            self.label54.grid(column=0,row=0,padx=10,pady=15)
            self.combobox54=ttk.Combobox(self.frame52,values=[i for i in range(1,100)],width=8,font=("等线",11))
            self.combobox54.grid(column=1,row=0,padx=5,pady=15)
            self.combobox54.current(0)
            self.combobox54.bind("<Enter>",func=info_get)
            self.label55=ttk.Label(self.frame52,text="个",font=("等线",13))
            self.label55.grid(column=2,row=0,padx=5,pady=15)
            self.combobox55=ttk.Combobox(self.frame52,values=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"],width=8,font=("等线",11))
            self.combobox55.grid(column=3,row=0,padx=5,pady=15)
            self.combobox55.current(0)
            self.combobox55.bind("<Enter>",func=info_get)
            self.label56=ttk.Label(self.frame52,text="后是",font=("等线",13))
            self.label56.grid(column=4,row=0,padx=5,pady=15)
            self.label57=ttk.Label(self.frame52,text="Hello!",font=("等线",17,"bold"),foreground="#FFA500")
            self.label57.grid(column=5,row=0,padx=20,pady=15)

            self.button51=ttk.Button(self.frame52,text="点击进行计算",style="font.TButton",command=mode5)
            self.button51.grid(column=0,row=1,columnspan=2,padx=10,pady=20,ipadx=5,ipady=5)

            self.db()
    
    def mm6(self,event=None):
        def info_get(event=None):
            y=self.combobox61.get()
            m=self.combobox62.get()
            d=self.combobox63.get()
            self.combobox63.configure(values=[i for i in range(1,mo.month(int(m),int(y))+1)])
            ly=self.combobox64.get()
            lm=self.combobox65.get()
            ld=self.combobox66.get()
            self.combobox65.configure(values=m6.months(int(ly)))
            self.combobox66.configure(values=m6.days(int(ly),lm))
            return y,m,d,ly,lm,ld
        def mode6stol(event=None):
            y,m,d,ly,lm,ld=info_get()
            lmonth,lday=m6.Lu(int(y),int(m),int(d)).s_to_l()
            n=m6.yy(y)
            self.label65.configure(text=f"{lmonth} {lday},是 {n[0]} 年({n[1]}年)")
        def mode6ltos(event=None):
            y,m,d,ly,lm,ld=info_get()
            lmname={"正月":1,"二月":2,"三月":3,"四月":4,"五月":5,"六月":6,"七月":7,"八月":8,"九月":9,"十月":10,"冬月":11,"腊月":12}
            ldname={"初一":1,"初二":2,"初三":3,"初四":4,"初五":5,"初六":6,"初七":7,"初八":8,"初九":9,"初十":10,
                    "十一":11,"十二":12,"十三":13,"十四":14,"十五":15,"十六":16,"十七":17,"十八":18,"十九":19,"二十":20,
                    "廿一":21,"廿二":22,"廿三":23,"廿四":24,"廿五":25,"廿六":26,"廿七":27,"廿八":28,"廿九":29,"三十":30}
            year,month,day=m6.Lu(int(ly),lmname[lm],ldname[ld]).l_to_s()
            n=m6.yy(year)
            self.label68.configure(text=f"{year}年{month}月{day}日,是 {n[0]} 年({n[1]}年)")
        def tp(event):
            self.table=[self.table61,6]

        style6=ttk.Style()
        style6.configure("font.TButton",font=("等线",14,"bold"),foreground="#1E90FF")
        if self.table_info[6]<1:
            self.table_info[6]=1
            self.table61=ttk.Frame(self.note)
            self.table61.bind("<Enter>",func=tp)
            self.table_list.append([self.table61,6])
            self.note.add(self.table61,text="模式6")

            self.scrollbar61=ttk.Scrollbar(self.table61,orient="vertical")
            self.c61=tk.Canvas(self.table61,yscrollcommand=self.scrollbar61.set,width=self.note.winfo_width()-30,height=self.note.winfo_height())
            self.f61=ttk.Frame(self.c61)
            self.c61.create_window(0,0,window=self.f61,anchor="nw")
            self.scrollbar61.configure(command=self.c61.yview)
            self.scrollbar61.grid(column=1,row=0,sticky="ns")
            self.c61.grid(column=0,row=0)
            window.update()
            self.c61.config(scrollregion=self.c.bbox("all"))

            self.frame61=ttk.Frame(self.f61)
            self.frame61.grid(column=0,row=0,sticky="ew")
            self.combobox61=ttk.Combobox(self.frame61,values=[i for i in range(1900,2100)],width=10,font=("等线",11))
            self.combobox61.grid(column=0,row=0,padx=10,pady=15)
            self.combobox61.current(100)
            self.combobox61.bind("<Enter>",func=info_get)
            self.label61=ttk.Label(self.frame61,text="年",font=("等线",13))
            self.label61.grid(column=1,row=0,padx=5,pady=15)
            self.combobox62=ttk.Combobox(self.frame61,values=[i for i in range(1,13)],width=10,font=("等线",11))
            self.combobox62.grid(column=2,row=0,padx=5,pady=15)
            self.combobox62.current(0)
            self.combobox62.bind("<Enter>",func=info_get)
            self.label62=ttk.Label(self.frame61,text="月",font=("等线",13))
            self.label62.grid(column=3,row=0,padx=5,pady=15)
            self.combobox63=ttk.Combobox(self.frame61,values=[i+1 for i in range(mo.month(1,2020))],width=10,font=("等线",11))
            self.combobox63.grid(column=4,row=0,padx=5,pady=15)
            self.combobox63.current(0)
            self.combobox63.bind("<Enter>",func=info_get)
            self.label63=ttk.Label(self.frame61,text="日",font=("等线",13))
            self.label63.grid(column=5,row=0,padx=5,pady=15)
            self.frame62=ttk.Frame(self.f61)
            self.frame62.grid(column=0,row=1,sticky="ew")
            self.label64=ttk.Label(self.frame62,text="转化为农历是",font=("等线",13))
            self.label64.grid(column=0,row=0,padx=10,pady=15)
            self.label65=ttk.Label(self.frame62,text="在这里显示农历日期哦",font=("等线",17,"bold"),foreground="#FFA500")
            self.label65.grid(column=1,row=0,padx=20,pady=15)
            self.button61=ttk.Button(self.frame62,text="点击转换",style="font.TButton",command=mode6stol)
            self.button61.grid(column=0,row=1,padx=10,pady=20,ipadx=5,ipady=5)
            self.frame63=ttk.Frame(self.f61)
            self.frame63.grid(column=0,row=2,sticky="ew")
            self.combobox64=ttk.Combobox(self.frame63,values=[i for i in range(1900,2100)],width=10,font=("等线",11))
            self.combobox64.grid(column=0,row=0,padx=10,pady=15)
            self.combobox64.current(100)
            self.combobox64.bind("<Enter>",func=info_get)
            self.label66=ttk.Label(self.frame63,text="年",font=("等线",13))
            self.label66.grid(column=1,row=0,padx=5,pady=15)
            self.combobox65=ttk.Combobox(self.frame63,values=["正月","二月","三月","四月","五月","六月","七月","八月","九月","十月","冬月","腊月"],width=10,font=("等线",11))
            self.combobox65.grid(column=2,row=0,padx=5,pady=15)
            self.combobox65.current(0)
            self.combobox65.bind("<Enter>",func=info_get)
            self.combobox66=ttk.Combobox(self.frame63,values=["初一"],width=10,font=("等线",11))
            self.combobox66.grid(column=4,row=0,padx=5,pady=15)
            self.combobox66.current(0)
            self.combobox66.bind("<Enter>",func=info_get)
            self.frame64=ttk.Frame(self.f61)
            self.frame64.grid(column=0,row=3,sticky="ew")
            self.label67=ttk.Label(self.frame64,text="转化为阳历是",font=("等线",13))
            self.label67.grid(column=0,row=0,padx=10,pady=15)
            self.label68=ttk.Label(self.frame64,text="在这里显示阳历日期哦",font=("等线",17,"bold"),foreground="#FFA500")
            self.label68.grid(column=1,row=0,padx=20,pady=15)
            self.button62=ttk.Button(self.frame64,text="点击转换",style="font.TButton",command=mode6ltos)
            self.button62.grid(column=0,row=1,padx=10,pady=20,ipadx=5,ipady=5)
            self.frame65=ttk.Frame(self.f61)
            self.frame65.grid(column=0,row=4,sticky="ew")
            self.label69=ttk.Label(self.frame65,text="注意事项:                          ",font=("方正粗黑宋简体",18,"bold"),foreground="#FF4500")
            self.label69.grid(column=0,row=0,pady=15)
            self.label610=ttk.Label(self.frame65,text="        ①由于作者太菜只能实现\n    1900到2100年之间的农历阳历转换\n        ②并且不要尝试一些极值，\n    比如2100.12.30这样的\n    （鬼知道会发生什么）",font=("幼圆",18),foreground="#FF4500")
            self.label610.grid(column=0,row=1,padx=5)
            self.db()

    def mm7(self,event=None):
        def info_get(event=None):
            h1=self.combobox71.get()
            m1=self.combobox72.get()
            s1=self.combobox73.get()
            h2=self.combobox74.get()
            m2=self.combobox75.get()
            s2=self.combobox76.get()
            return h1,m1,s1,h2,m2,s2
        def mode7(event=None):
            h1,m1,s1,h2,m2,s2=info_get()
            ns=m7.m7(int(h1),int(m1),int(s1),int(h2),int(m2),int(s2))
            self.label78.configure(text=str(ns[0])+" 秒")
            self.label710.configure(text=f"{ns[1][0]} 时 {ns[1][1]} 分 {ns[1][2]} 秒")
        def tp(event):
            self.table=[self.table71,7]

        style7=ttk.Style()
        style7.configure("font.TButton",font=("等线",13,"bold"),foreground="#1E90FF")
        if self.table_info[7]<1:
            self.table_info[7]=1
            self.table71=ttk.Frame(self.note)
            self.table71.bind("<Enter>",func=tp)
            self.table_list.append([self.table71,7])
            self.note.add(self.table71,text="模式7")
            self.frame71=ttk.Frame(self.table71)
            self.frame71.grid(column=0,row=0,sticky="ew")
            self.combobox71=ttk.Combobox(self.frame71,values=[i for i in range(0,25)],width=10,font=("等线",11))
            self.combobox71.grid(column=0,row=0,padx=10,pady=15)
            self.combobox71.current(0)
            self.combobox71.bind("<Enter>",func=info_get)
            self.label71=ttk.Label(self.frame71,text="时",font=("等线",13))
            self.label71.grid(column=1,row=0,padx=5,pady=15)
            self.combobox72=ttk.Combobox(self.frame71,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox72.grid(column=2,row=0,padx=5,pady=15)
            self.combobox72.current(0)
            self.combobox72.bind("<Enter>",func=info_get)
            self.label72=ttk.Label(self.frame71,text="分",font=("等线",13))
            self.label72.grid(column=3,row=0,padx=5,pady=15)
            self.combobox73=ttk.Combobox(self.frame71,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox73.grid(column=4,row=0,padx=5,pady=15)
            self.combobox73.current(0)
            self.combobox73.bind("<Enter>",func=info_get)
            self.label73=ttk.Label(self.frame71,text="秒",font=("等线",13))
            self.label73.grid(column=5,row=0,padx=5,pady=15)
            self.frame72=ttk.Frame(self.table71)
            self.frame72.grid(column=0,row=1,sticky="ew")
            self.combobox74=ttk.Combobox(self.frame72,values=[i for i in range(0,25)],width=10,font=("等线",11))
            self.combobox74.grid(column=0,row=0,padx=10,pady=15)
            self.combobox74.current(0)
            self.combobox74.bind("<Enter>",func=info_get)
            self.label74=ttk.Label(self.frame72,text="时",font=("等线",13))
            self.label74.grid(column=1,row=0,padx=5,pady=15)
            self.combobox75=ttk.Combobox(self.frame72,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox75.grid(column=2,row=0,padx=5,pady=15)
            self.combobox75.current(0)
            self.combobox75.bind("<Enter>",func=info_get)
            self.label75=ttk.Label(self.frame72,text="分",font=("等线",13))
            self.label75.grid(column=3,row=0,padx=5,pady=15)
            self.combobox76=ttk.Combobox(self.frame72,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox76.grid(column=4,row=0,padx=5,pady=15)
            self.combobox76.current(0)
            self.combobox76.bind("<Enter>",func=info_get)
            self.label76=ttk.Label(self.frame72,text="秒",font=("等线",13))
            self.label76.grid(column=5,row=0,padx=5,pady=15)
            self.frame73=ttk.Frame(self.table71)
            self.frame73.grid(column=0,row=2,sticky="ew")
            self.label77=ttk.Label(self.frame73,text="之间相隔",font=("等线",13))
            self.label77.grid(column=0,row=0,padx=10,pady=15)
            self.label78=ttk.Label(self.frame73,text="uwu",font=("等线",17,"bold"),foreground="#FFA500")
            self.label78.grid(column=1,row=0,padx=20,pady=15)
            self.label79=ttk.Label(self.frame73,text="或者这么说",font=("等线",13))
            self.label79.grid(column=2,row=0,padx=10,pady=15)
            self.label710=ttk.Label(self.frame73,text="awa",font=("等线",17,"bold"),foreground="#FFA500")
            self.label710.grid(column=3,row=0,padx=10,pady=15)

            self.button71=ttk.Button(self.frame73,text="点击进行计算",style="font.TButton",command=mode7)
            self.button71.grid(column=0,row=1,columnspan=2,padx=10,pady=20,ipadx=5,ipady=5)
            self.db()

    def mm8(self,event=None):
        def info_get(event=None):
            y2=self.combobox81.get()
            return y2
        def mode8(event=None):
            time=datetime.date.today()
            y1=time.year
            mo1=time.month
            d1=time.day
            y2=info_get()
            n=m8.m8(y1,mo1,d1,int(y2))
            t=str(n)+" 天"
            if int(y2)<y1:
                t="-"+t
            elif y2==y1:
                if mo1<6:
                    t="-"+t
                elif mo1==6:
                    if d1<6:
                        t="-"+t
            if n>100:
                self.label83.configure(text=t,foreground="red",font=("等线",80,"bold"))
            else:
                self.label83.configure(text=t+"!!!!!",foreground="#8B0000",font=("等线",80,"bold"))
        def tp(event):
            self.table=[self.table81,8]

        style8=ttk.Style()
        style8.configure("font.TButton",font=("等线",13,"bold"),foreground="#CD5C5C")
        if self.table_info[8]<1:
            self.table_info[8]=1
            self.table81=ttk.Frame(self.note)
            self.table81.bind("<Enter>",func=tp)
            self.table_list.append([self.table81,8])
            self.note.add(self.table81,text="模式8")
            self.frame81=ttk.Frame(self.table81)
            self.frame81.grid(column=0,row=0,sticky="ew")
            self.label81=ttk.Label(self.frame81,text="距离",font=("等线",13))
            self.label81.grid(column=0,row=0,padx=10,pady=10)
            self.combobox81=ttk.Combobox(self.frame81,values=[i for i in range(2000,2100)],width=10,font=("等线",11))
            self.combobox81.grid(column=1,row=0,padx=10,pady=15)
            self.combobox81.current(23)
            self.label82=ttk.Label(self.frame81,text="年的高考还剩",font=("等线",13))
            self.label82.grid(column=2,row=0,padx=10,pady=10)
            self.frame82=ttk.Frame(self.table81)
            self.frame82.grid(column=0,row=1,sticky="ew")
            self.label83=ttk.Label(self.frame82,text="看啥看，复习去！",font=("等线",50,"bold"),foreground="red")
            self.label83.grid(column=0,row=0,padx=20,pady=20)
            self.frame83=ttk.Frame(self.table81)
            self.frame83.grid(column=0,row=2,sticky="ew")

            self.button81=ttk.Button(self.frame83,text="点击来点压迫感",style="font.TButton",command=mode8)
            self.button81.grid(column=0,row=1,columnspan=2,padx=10,pady=40,ipadx=5,ipady=5)
            self.db()

    def mm9(self,event=None):
        def info_get(event=None):
            h1=self.combobox91.get()
            mo1=self.combobox92.get()
            s1=self.combobox93.get()
            h2=self.combobox94.get()
            mo2=self.combobox95.get()
            s2=self.combobox96.get()
            s=self.combobox97.get()
            return h1,mo1,s1,h2,mo2,s2,s
        def mode9(event=None):
            h1,mo1,s1,h2,mo2,s2,s=info_get()
            if self.n9==0:
                n=m9.m9(int(h1),int(mo1),int(s1),int(h2),int(mo2),int(s2))
                self.n9=1
            else:
                n=m9.m9s(int(h1),int(mo1),int(s1),int(s))
                self.n9=0
            if n[1]==0:
                self.label96.configure(text=f"{n[0][0]} 时 {n[0][1]} 分 {n[0][2]} 秒")
            else:
                self.label96.configure(text=f"{n[1]} 天后的 {n[0][0]} 时 {n[0][1]} 分 {n[0][2]} 秒")
        def tp(event):
            self.table=[self.table91,9]

        style9=ttk.Style()
        style9.configure("font.TButton",font=("等线",13,"bold"),foreground="#1E90FF")
        self.n9=0
        if self.table_info[9]<1:
            self.table_info[9]=1
            self.table91=ttk.Frame(self.note)
            self.table91.bind("<Enter>",func=tp)
            self.table_list.append([self.table91,9])
            self.note.add(self.table91,text="模式9")
            self.frame91=ttk.Frame(self.table91)
            self.frame91.grid(column=0,row=0,sticky="ew")
            self.combobox91=ttk.Combobox(self.frame91,values=[i for i in range(0,25)],width=10,font=("等线",11))
            self.combobox91.grid(column=0,row=0,padx=10,pady=15)
            self.combobox91.current(0)
            self.combobox91.bind("<Enter>",func=info_get)
            self.label91=ttk.Label(self.frame91,text="时",font=("等线",13))
            self.label91.grid(column=1,row=0,padx=5,pady=15)
            self.combobox92=ttk.Combobox(self.frame91,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox92.grid(column=2,row=0,padx=5,pady=15)
            self.combobox92.current(0)
            self.combobox92.bind("<Enter>",func=info_get)
            self.label92=ttk.Label(self.frame91,text="分",font=("等线",13))
            self.label92.grid(column=3,row=0,padx=5,pady=15)
            self.combobox93=ttk.Combobox(self.frame91,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox93.grid(column=4,row=0,padx=5,pady=15)
            self.combobox93.current(0)
            self.combobox93.bind("<Enter>",func=info_get)
            self.label93=ttk.Label(self.frame91,text="秒， 在",font=("等线",13))
            self.label93.grid(column=5,row=0,padx=5,pady=15)
            self.frame92=ttk.Frame(self.table91)
            self.frame92.grid(column=0,row=1,sticky="ew")
            self.combobox94=ttk.Combobox(self.frame92,values=[i for i in range(0,25)],width=10,font=("等线",11))
            self.combobox94.grid(column=0,row=0,padx=10,pady=15)
            self.combobox94.current(0)
            self.combobox94.bind("<Enter>",func=info_get)
            self.label94=ttk.Label(self.frame92,text="时",font=("等线",13))
            self.label94.grid(column=1,row=0,padx=5,pady=15)
            self.combobox95=ttk.Combobox(self.frame92,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox95.grid(column=2,row=0,padx=5,pady=15)
            self.combobox95.current(0)
            self.combobox95.bind("<Enter>",func=info_get)
            self.label95=ttk.Label(self.frame92,text="分",font=("等线",13))
            self.label95.grid(column=3,row=0,padx=5,pady=15)
            self.combobox96=ttk.Combobox(self.frame92,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox96.grid(column=4,row=0,padx=5,pady=15)
            self.combobox96.current(0)
            self.combobox96.bind("<Enter>",func=info_get)
            self.label96=ttk.Label(self.frame92,text="秒， 或者",font=("等线",13))
            self.label96.grid(column=5,row=0,padx=5,pady=15)
            self.frame93=ttk.Frame(self.table91)
            self.frame93.grid(column=0,row=2,sticky="ew")
            self.combobox97=ttk.Combobox(self.frame93,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox97.grid(column=0,row=0,padx=5,pady=15)
            self.combobox97.current(0)
            self.combobox97.bind("<Enter>",func=info_get)
            self.label97=ttk.Label(self.frame93,text="秒， 后是",font=("等线",13))
            self.label97.grid(column=1,row=0,padx=10,pady=15)
            self.label96=ttk.Label(self.frame93,text="xx 时 xx 分 xx 秒",font=("等线",17,"bold"),foreground="#FFA500")
            self.label96.grid(column=2,row=0,padx=20,pady=15)

            self.frame94=ttk.Frame(self.table91)
            self.frame94.grid(column=0,row=3,sticky="ew")
            self.button91=ttk.Button(self.frame94,text="点击进行计算(先计算第一个，再次点击计算第二个)",style="font.TButton",command=mode9)
            self.button91.grid(column=0,row=0,columnspan=2,padx=10,pady=40,ipadx=5,ipady=5)
            self.db()

    def mm10(self,event=None):
        def info_get(event=None):
            s=self.combobox101.get()
            ds=self.combobox102.get()
            return int(s),float(ds)
        def mode10(event=None):
            s,ds=info_get()
            #m10.m10(int(s),int(ds))写了个没用的.py文件...
            start_time=time.perf_counter()
            while time.perf_counter()-start_time<=s:
                if round(time.perf_counter()-start_time,2)%ds==0:
                    playsound.play("tickshort.wav")
                    time.sleep(ds/2)
        def tp(event):
            self.table=[self.table101,10]

        style10=ttk.Style()
        style10.configure("font.TButton",font=("等线",13,"bold"),foreground="#1E90FF")
        if self.table_info[10]<1:
            self.table_info[10]=1
            self.table101=ttk.Frame(self.note)
            self.table101.bind("<Enter>",func=tp)
            self.table_list.append([self.table101,10])
            self.note.add(self.table101,text="模式10")
            self.frame101=ttk.Frame(self.table101)
            self.frame101.grid(column=0,row=0,sticky="ew")
            self.label101=ttk.Label(self.frame101,text="总时长为",font=("等线",13))
            self.label101.grid(column=0,row=0,padx=10,pady=15)
            self.combobox101=ttk.Combobox(self.frame101,values=[i for i in range(0,3600)],width=10,font=("等线",11))
            self.combobox101.grid(column=1,row=0,padx=5,pady=15)
            self.combobox101.current(0)
            self.combobox101.bind("<Enter>",func=info_get)
            self.label102=ttk.Label(self.frame101,text="秒",font=("等线",13))
            self.label102.grid(column=2,row=0,padx=5,pady=15)
            self.label103=ttk.Label(self.frame101,text="每",font=("等线",13))
            self.label103.grid(column=3,row=0,padx=15,pady=15)
            self.combobox102=ttk.Combobox(self.frame101,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox102.grid(column=4,row=0,padx=5,pady=15)
            self.combobox102.current(0)
            self.combobox102.bind("<Enter>",func=info_get)
            self.label104=ttk.Label(self.frame101,text="秒报一次时",font=("等线",13))
            self.label104.grid(column=5,row=0,padx=5,pady=15)
            self.frame102=ttk.Frame(self.table101)
            self.frame102.grid(column=0,row=1,sticky="ew")
            self.button101=ttk.Button(self.frame102,text="点击开始",style="font.TButton",command=mode10)
            self.button101.grid(column=0,row=0,columnspan=2,padx=10,pady=15,ipadx=4,ipady=5)
            self.label105=ttk.Label(self.frame102,text="可以使用小数哦(声音可能有点小)",font=("等线",14),foreground="green")
            self.label105.grid(column=2,row=0,columnspan=2,padx=5,pady=15)

            self.db()
    
    def mm11(self,event=None):
        def info_get(enent=None):
            h=self.combobox111.get()
            m=self.combobox112.get()
            s1=self.combobox113.get()
            s2=self.combobox114.get()
            return int(h),int(m),int(s1),int(s2)
        def mode11(event=None):
            h,m,s1,s2=info_get()
            n=m11.m11(h,m,s1)
            self.label115.configure(text=n)
        def mode11s(event=None):
            h,m,s1,s2=info_get()
            n=m11.m11s(s2)
            self.label119.configure(text=f"{n[0]} 时 {n[1]} 分 {n[2]} 秒")
        def tp(event):
            self.table=[self.table111,11]

        style11=ttk.Style()
        style11.configure("font.TButton",font=("等线",13,"bold"),foreground="#1E90FF")
        if self.table_info[11]<1:
            self.table_info[11]=1
            self.table111=ttk.Frame(self.note)
            self.table111.bind("<Enter>",func=tp)
            self.table_list.append([self.table111,11])
            self.note.add(self.table111,text="模式11")
            self.frame111=ttk.Frame(self.table111)
            self.frame111.grid(column=0,row=0,sticky="ew")
            self.combobox111=ttk.Combobox(self.frame111,values=[i for i in range(0,25)],width=10,font=("等线",11))
            self.combobox111.grid(column=0,row=0,padx=10,pady=15)
            self.combobox111.current(0)
            self.combobox111.bind("<Enter>",func=info_get)
            self.label111=ttk.Label(self.frame111,text="时",font=("等线",13))
            self.label111.grid(column=1,row=0,padx=5,pady=15)
            self.combobox112=ttk.Combobox(self.frame111,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox112.grid(column=2,row=0,padx=5,pady=15)
            self.combobox112.current(0)
            self.combobox112.bind("<Enter>",func=info_get)
            self.label112=ttk.Label(self.frame111,text="分",font=("等线",13))
            self.label112.grid(column=3,row=0,padx=5,pady=15)
            self.combobox113=ttk.Combobox(self.frame111,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox113.grid(column=4,row=0,padx=5,pady=15)
            self.combobox113.current(0)
            self.combobox113.bind("<Enter>",func=info_get)
            self.label113=ttk.Label(self.frame111,text="秒",font=("等线",13))
            self.label113.grid(column=5,row=0,padx=5,pady=15)
            self.frame112=ttk.Frame(self.table111)
            self.frame112.grid(column=0,row=1,sticky="ew")
            self.label114=ttk.Label(self.frame112,text="转化为秒是",font=("等线",13))
            self.label114.grid(column=0,row=0,padx=10,pady=15)
            self.label115=ttk.Label(self.frame112,text="233",font=("等线",17,"bold"),foreground="#FFA500")
            self.label115.grid(column=1,row=0,padx=20,pady=15)
            self.label116=ttk.Label(self.frame112,text="秒",font=("等线",13))
            self.label116.grid(column=2,row=0,padx=10,pady=15)
            self.button111=ttk.Button(self.frame112,text="点击进行计算",style="font.TButton",command=mode11)
            self.button111.grid(column=3,row=0,columnspan=2,padx=35,pady=15,ipadx=5,ipady=5)
            self.frame113=ttk.Frame(self.table111)
            self.frame113.grid(column=0,row=2,sticky="ew")
            self.combobox114=ttk.Combobox(self.frame113,values=[i for i in range(0,3600)],width=10,font=("等线",11))
            self.combobox114.grid(column=0,row=0,padx=10,pady=15)
            self.combobox114.current(0)
            self.combobox114.bind("<Enter>",func=info_get)
            self.label117=ttk.Label(self.frame113,text="秒",font=("等线",13))
            self.label117.grid(column=1,row=0,padx=5,pady=15)
            self.frame114=ttk.Frame(self.table111)
            self.frame114.grid(column=0,row=3,sticky="ew")
            self.label118=ttk.Label(self.frame114,text="转化为时分秒是",font=("等线",13))
            self.label118.grid(column=0,row=0,padx=10,pady=15)
            self.label119=ttk.Label(self.frame114,text="= )",font=("等线",17,"bold"),foreground="#FFA500")
            self.label119.grid(column=1,row=0,padx=20,pady=15)
            self.button112=ttk.Button(self.frame114,text="点击进行计算",style="font.TButton",command=mode11s)
            self.button112.grid(column=2,row=0,columnspan=2,padx=35,pady=15,ipadx=5,ipady=5)

            self.db()

    def mm12(self,event=None):
        def mode12_start(event=None):
            self.t.start()
        def mode12_stop(event=None):
            self.t.stop()
        def mode12_clear(event=None):
            self.label121.configure(text="00:00:00.00")
            self.t.clear()
        def tp(event):
            self.table=[self.table121,12]

        style12=ttk.Style()
        style12.configure("font.TButton",font=("等线",15,"bold"),foreground="#1E90FF")
        if self.table_info[12]<1:
            self.table_info[12]=1
            self.table121=ttk.Frame(self.note)
            self.table121.bind("<Enter>",func=tp)
            self.table_list.append([self.table121,12])
            self.note.add(self.table121,text="模式12")
            self.frame121=ttk.Frame(self.table121)
            self.frame121.grid(column=0,row=0,sticky="ew")
            self.label121=ttk.Label(self.frame121,text="00:00:00.00",font=("等线",70))
            self.label121.grid(column=0,row=0,padx=50,pady=50)
            self.frame122=ttk.Frame(self.table121)
            self.frame122.grid(column=0,row=1,sticky="ew")
            self.text121="点击开始计时"
            self.button121=ttk.Button(self.frame122,text=self.text121,style="font.TButton",command=mode12_start)
            self.button121.grid(column=0,row=0,padx=35,pady=20,ipadx=5,ipady=5)
            self.text122="暂停"
            self.button122=ttk.Button(self.frame122,text=self.text122,style="font.TButton",command=mode12_stop)
            self.button122.grid(column=1,row=0,padx=30,pady=20,ipadx=15,ipady=5)
            self.text123="结束"
            self.button123=ttk.Button(self.frame122,text=self.text123,style="font.TButton",command=mode12_clear)
            self.button123.grid(column=2,row=0,padx=30,pady=20,ipadx=15,ipady=5)
            self.t=m12.m12(self,self.label121,self.text122)

            self.db()
    
    def mm13(self,event=None):
        def mode13_start(event=None):
            self.t=m13.m13(self,self.time,self.label131,self.text132)
            self.t.start()
        def mode13_stop(event=None):
            self.t.stop()
        def mode13_clear(event=None):
            self.label131.configure(text="00:00:00")
            self.t.clear()
        def info_get(event=None):
            h=int(self.combobox131.get())
            m=int(self.combobox132.get())
            s=int(self.combobox133.get())
            while s>=60:
                s-=60
                m+=1
            while m>=60:
                m-=60
                h+=1
            self.time=m11.m11(h,m,s)
            h,m,s=str(h),str(m),str(s)
            if len(s)==1:
                s="0"+s
            if len(m)==1:
                m="0"+m
            if len(h)==1:
                h="0"+h
            elif len(h)>2:
                self.label131.configure(font=("等线",70-10*(len(h)-2)))
            self.label131.configure(text=f"{h}:{m}:{s}.00")
            return self.time
        def mode13_set(event=None):
            self.top=tk.Toplevel(self.table131)
            self.combobox131=ttk.Combobox(self.top,values=[i for i in range(0,100)],width=10,font=("等线",11))
            self.combobox131.grid(column=0,row=0,padx=10,pady=15)
            self.combobox131.current(0)
            self.combobox131.bind("<Enter>",func=info_get)
            self.label132=ttk.Label(self.top,text="时",font=("等线",13))
            self.label132.grid(column=1,row=0,padx=5,pady=15)
            self.combobox132=ttk.Combobox(self.top,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox132.grid(column=2,row=0,padx=10,pady=15)
            self.combobox132.current(0)
            self.combobox132.bind("<Enter>",func=info_get)
            self.label133=ttk.Label(self.top,text="分",font=("等线",13))
            self.label133.grid(column=3,row=0,padx=5,pady=15)
            self.combobox133=ttk.Combobox(self.top,values=[i for i in range(0,60)],width=10,font=("等线",11))
            self.combobox133.grid(column=4,row=0,padx=10,pady=15)
            self.combobox133.current(0)
            self.combobox133.bind("<Enter>",func=info_get)
            self.label134=ttk.Label(self.top,text="秒",font=("等线",13))
            self.label134.grid(column=5,row=0,padx=5,pady=15)
            self.button135=ttk.Button(self.top,text="确认",style="font.TButton",command=info_get)
            self.button135.grid(column=6,row=0,padx=5,pady=15,ipadx=5,ipady=5)
        def tp(event):
            self.table=[self.table131,13]

        style13=ttk.Style()
        style13.configure("font.TButton",font=("等线",15,"bold"),foreground="#1E90FF")
        if self.table_info[13]<1:
            self.table_info[13]=1
            self.table131=ttk.Frame(self.note)
            self.table131.bind("<Enter>",func=tp)
            self.table_list.append([self.table131,13])
            self.note.add(self.table131,text="模式13")
            self.frame131=ttk.Frame(self.table131)
            self.frame131.grid(column=0,row=0,sticky="ew")
            self.label131=ttk.Label(self.frame131,text="00:00:00.00",font=("等线",70))
            self.label131.grid(column=0,row=0,padx=50,pady=50)
            self.frame132=ttk.Frame(self.table131)
            self.frame132.grid(column=0,row=1,sticky="ew")
            self.text131="点击开始倒计时"
            self.button131=ttk.Button(self.frame132,text=self.text131,style="font.TButton",command=mode13_start)
            self.button131.grid(column=0,row=0,padx=35,pady=20,ipadx=5,ipady=5)
            self.text132="暂停"
            self.button132=ttk.Button(self.frame132,text=self.text132,style="font.TButton",command=mode13_stop)
            self.button132.grid(column=1,row=0,padx=30,pady=20,ipadx=15,ipady=5)
            self.text133="结束"
            self.button133=ttk.Button(self.frame132,text=self.text133,style="font.TButton",command=mode13_clear)
            self.button133.grid(column=2,row=0,padx=30,pady=20,ipadx=15,ipady=5)
            self.frame133=ttk.Frame(self.table131)
            self.frame133.grid(column=0,row=2,sticky="ew")
            self.button134=ttk.Button(self.frame133,text="点击设置时间",style="font.TButton",command=mode13_set)
            self.button134.grid(column=0,row=0,padx=35,pady=20,ipadx=170,ipady=5,sticky="ew")
            self.top=None
            self.combobox131=None
            self.label132=None
            self.combobox132=None
            self.label133=None
            self.combobox133=None
            self.label134=None
            self.button135=None
            self.t=m13.m13(self,0,self.label131,self.text132)
            self.time=0

            self.db()

if __name__=="__main__":
    window=tk.Tk(className=" Time Master  丨  BY de3BDJMH")
    window.geometry("900x600")
    window.resizable(False,False)
    window.iconbitmap('time.ico')

    window.tk.call("source", "sun-valley.tcl")
    window.tk.call("set_theme", "light")

    app=App(window).grid()

tk.mainloop()