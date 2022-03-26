import time
import playsound
start_time=time.perf_counter()
def m10(s,ds):
    while time.perf_counter()-start_time<=s:
        if round(time.perf_counter()-start_time,2)%ds==0:
            #print(chr(7))#响铃
            playsound.play("tickshort.wav")
            time.sleep(ds/2)