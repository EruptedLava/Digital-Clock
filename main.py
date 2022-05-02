from digits import d
from datetime import datetime
import time
import os
import colorama
from colorama import Fore
import random
import platform
colorama.init()

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
# ctl = list(current_time)
# print(ctl)

if platform.system() == "Windows":
    cmd = "cls"
else:
    cmd = "clear"

colorss = [Fore.GREEN, Fore.RED, Fore.BLUE,Fore.CYAN,Fore.MAGENTA, Fore.WHITE,Fore.LIGHTYELLOW_EX,Fore.LIGHTGREEN_EX,Fore.LIGHTMAGENTA_EX,Fore.LIGHTBLACK_EX]

def timeee():
    os.system(cmd)
    print(random.choice(colorss)+"\n\n\n\n\n\n\n\n")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ctl = list(current_time)
    for _ in range(8):
        print(d['s'][_],d['s'][_],d['s'][_],d['s'][_],d[ctl[0]][_],d[ctl[1]][_],d[ctl[2]][_],d[ctl[3]][_],d[ctl[4]][_],d[ctl[5]][_],d[ctl[6]][_],d[ctl[7]][_])

while True:
    time.sleep(1)
    timeee()
