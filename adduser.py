from AnbarFinal.wsgi import *
from authentication.views import createuser

b=open('adduser.txt','r')
readline=b.read().splitlines()

username1=readline[0]
pass11=readline[1]
myuser = createuser(username1, "", pass11)
b.close()