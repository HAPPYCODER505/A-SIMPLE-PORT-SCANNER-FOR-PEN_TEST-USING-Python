#hallo friends it is a very simple port scanner.

import sys
import  socket
import threading
from datetime import  datetime

usage = "python port scanner: PLEASE GIVE: (TARGET IP),(START PORT),(END PORT)"

print("-"*70)
print("python port scanner")
print("-"*70)
if(len(sys.argv)!=4):
    print(usage)
    sys.exit()
try :
    targ= socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("name resolution error")
    sys.exit()
startpo= int(sys.argv[2])
endpo=int(sys.argv[3])

print("scani target", targ)
def scanport(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(5)
    conn=s.connect_ex((targ,port))
    if(not conn):
        print("port {} is open".format(port))
    s.close()
for port in range(startpo,endpo+1):
    thred=threading.Thread(target = scanport,args=(port,))
    thred.daemon = True
    thred.start()


