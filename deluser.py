from AnbarFinal.wsgi import *
from authentication.views import deluser

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AnbarFinal.settings")
#django.setup()
b=open('deluser.txt','r')
readline=b.read().splitlines()
username1=readline[0]
deluser(username1)