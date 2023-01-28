from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.models import coinfo, things
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            user1 = user.username
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html", {"fname": user1})
        else:
            messages.error(request, "نام کاربری و یا رمز عبور اشتباه است!")
            return redirect('home')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "با موفقیت خارج شدید!")
    return redirect('home')


def createuser(username, email, pass1):
    myuser = User.objects.create_user(username, email, pass1)
    myuser.save()

def deluser(username):
    myuser = User.objects.get(username=username)
    myuser.delete()
def place(request):
    if request.method=='POST':
        conumberorbillnum=request.POST['conum']
        coplace=request.POST['side']+'-'+request.POST['row']+'-'+request.POST['sec']
        current_user=str(request.user)
        try:
            if "xik" in conumberorbillnum :
                newcon = coinfo.objects.get(prodcode=conumberorbillnum)
                conumber=newcon.contnum
                newcon.sector = coplace
                newcon.save()
                newcon.lastuser = current_user
                newcon.save()
                messagesNEW = "جانگاری کانتینر {} در {} انجام شد!".format(conumber, coplace)
                messages.success(request, messagesNEW)
                return render(request, "authentication/place.html", {"fname": current_user})
            else:
                newcon = coinfo.objects.filter(billnum=conumberorbillnum)
                billnum = conumberorbillnum
                newcon.update(sector=f'{coplace}')

                newcon.update(lastuser=f'{current_user}')

                messagesNEW = "جانگاری کانتینر های قبض انبار {} در {} انجام شد!".format(billnum, coplace)
                messages.success(request, messagesNEW)
                return render(request, "authentication/place.html", {"fname": current_user})

        except Exception as e:
            print(e)
            messagesNEW = "شماره کانتینر و یا قبض انبار اشتباه است"
            messages.error(request, messagesNEW)

    return render(request, "authentication/place.html")
def reports(request):
    if request.method == 'POST':
        conumber = request.POST['conumber']
        try:
            newcon = coinfo.objects.get(prodcode=conumber)
            conumber = request.POST['conumber']
            conumber2 = str(newcon.contnum)
            billnumber2 = str(newcon.billnum)

            sector2 = str(newcon.sector)

            entertype2 = str(newcon.entertype)

            carrier2 = str(newcon.carrier)

            weight2 = str(newcon.weight)

            takhlie2 = str(newcon.takhlie)

            matrooke2 = str(newcon.matrooke)

            roozha2 = str(newcon.roozha)

            size2 = str(newcon.size)
            try:
                newcon2 = things.objects.get(contcode=conumber)
                prodname2 = str(newcon2.prodname)
                count2 = str(newcon2.count)
            except:
                prodname2 = 'اطلاعات موجود نیست'
                count2 = 'اطلاعات موجود نیست'
                # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/reportsresult.html",
                              {"conumber": conumber2, "billnum": billnumber2, "sector": sector2, "size": size2,
                               "entertype": entertype2, "roozha": roozha2, "matrooke": matrooke2, "prodname": prodname2,
                               "takhlie": takhlie2, "weight": weight2, "carrier": carrier2, "count": count2})
        except:
            messagesNEW = "شماره کانتینر اشتباه است"
            messages.error(request, messagesNEW)


        """tedad = newcon.count()
        print(tedad)
        for i in range(0, tedad):
            print(newcon[i].sector)
        print(type(newcon))"""




        # messages.success(request, "Logged In Sucessfully!!")


    return render(request, "authentication/reports.html")
def reportsresult(request):
    return render(request, "authentication/reportsresult.html")