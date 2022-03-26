import json
import tkinter
import time
class m12():
    def __init__(self,screen,label,text):
        self.config={"start":time.time(),"now":0,"stop":True,"isstart":False,"clear":True}
        self.screen=screen
        self.label=label
        self.text=text
        self.route="config\\m12.json"
    
    def start(self):
        self.config["start"]=time.time()
        self.config["stop"]=False
        self.config["isstart"]=True
        self.config["clear"]=False
        with open(self.route,"w") as c:
            json.dump(self.config,c)
        self.count()

    def count(self):
        with open(self.route) as c:
            config=json.load(c)
        while config["stop"]==False and config["isstart"]:
            with open(self.route) as c:
                config=json.load(c)
            self.config["now"]=time.time()-self.config["start"]
            s=str(round(self.config["now"],2)%60%60)[:5]
            m=str(int(self.config["now"]//60%60))
            h=str(int(self.config["now"]//60//60))
            if "." in s[:2]:
                s="0"+s
            if len(m)==1:
                m="0"+m
            if len(h)==1:
                h="0"+h
            elif len(h)>2:
                self.label.configure(font=("等线",70-10*(len(h)-2)))
            self.label.configure(text=f"{h}:{m}:{s}")
            self.screen.update()
            if config["clear"]:
                self.label.configure(text="00:00:00.00")
                self.screen.update()
                break
            with open(self.route,"w") as c:
                json.dump(self.config,c)
            
    def stop(self):
        with open(self.route) as c:
            config=json.load(c)
        if config["isstart"]:
            if self.text=="暂停":
                self.text="继续"
                self.config["stop"]=True
            elif self.text=="继续":
                self.text="暂停"
                self.config["stop"]=False
            self.screen.button122.configure(text=self.text)
        if self.text=="继续":
            self.config["start"]=time.time()-self.config["now"]
            with open(self.route,"w") as c:
                json.dump(self.config,c)
        elif self.text=="暂停":
            self.config["start"]=time.time()-self.config["now"]
            with open(self.route,"w") as c:
                json.dump(self.config,c)
            self.count()
    
    def clear(self):
        self.config={"start":time.time(),"now":0,"stop":True,"isstart":False,"clear":True}
        self.label.configure(text="00:00:00.00")
        self.text="暂停"
        self.screen.button122.configure(text=self.text)
        self.screen.update()