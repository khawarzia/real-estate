from django.shortcuts import render
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .tokens import account_activation_token
from functionality.models import properties


from .forms import *
from .models import *

def newfunc2(request,sel,val,usr):
    for i in profileModel.objects.all():
        if i.user.username == usr:
            obj = i
            break
    if (sel == 1):
        obj.minprice = int(val)
    elif (sel == 2):
        obj.maxprice = int(val)
    elif (sel == 3):
        obj.stories = int(val)
    elif (sel == 4):
        obj.minsqft = int(val)
    elif (sel == 5):
        obj.maxsqft = int(val)
    elif (sel == 6):
        obj.minlot = int(val)
    elif (sel == 7):
        obj.maxlot = int(val)
    elif (sel == 8):
        obj.property_type = val
    elif (sel == 9):
        obj.beds = int(val)
    elif (sel == 10):
        obj.bath = int(val)
    else:
        pass
    obj.save()
    return

def newfunc(request,sel,val):
    obj = profileModel.objects.get(user=request.user)
    if (sel == 1):
        obj.minprice = int(val)
    elif (sel == 2):
        obj.maxprice = int(val)
    elif (sel == 3):
        obj.stories = int(val)
    elif (sel == 4):
        obj.minsqft = int(val)
    elif (sel == 5):
        obj.maxsqft = int(val)
    elif (sel == 6):
        obj.minlot = int(val)
    elif (sel == 7):
        obj.maxlot = int(val)
    elif (sel == 8):
        obj.property_type = val
    elif (sel == 9):
        obj.beds = int(val)
    elif (sel == 10):
        obj.bath = int(val)
    else:
        pass
    obj.save()
    return

def form1(request):
    obj = User.objects.get(username=request.user.username)
    obj.first_name = request.POST['name']
    obj.email = request.POST['email']
    obj.save()
    obj = profileModel.objects.get(user=obj)
    obj.phone = request.POST['phone']
    obj.occupation = request.POST['occupation']
    obj.selopt = 0
    obj.save()
    return redirect('/my_profile')

def form2(request):
    obj = profileModel.objects.get(user=request.user)
    print(request.POST)
    try:
        a = request.POST['singlefamily']
        if a == 'on':
            obj.sf = True
    except:
        obj.sf = False
    try:
        b = request.POST['townhome']
        if b == 'on':
            obj.th = True
    except:
        obj.th = False
    try:
        c = request.POST['condominium']
        if c == 'on':
            obj.cd = True
    except:
        obj.cd = False
    try:
        d = request.POST['multifamily']
        if d == 'on':
            obj.mf = True
    except:
        obj.mf = False
    try:
        e = request.POST['land']
        if e == 'on':
            obj.ln = True
    except:
        obj.ln = False
    try:
        obj.minprice = request.POST['minprice']
    except:
        pass
    try:
        obj.maxprice = request.POST['maxprice']
    except:
        pass
    try:
        obj.stories = request.POST['stories']
    except:
        pass
    try:
        obj.minsqft = request.POST['minsqft']
    except:
        pass
    try:
        obj.maxsqft = request.POST['maxsqft']
    except:
        pass
    try:
        obj.minlot = request.POST['minlot']
    except:
        pass
    try:
        obj.maxlot = request.POST['maxlot']
    except:
        pass
    try:
        obj.beds = request.POST['maxbeds']
    except:
        pass
    try:
        obj.bath = request.POST['maxbath']
    except:
        pass
    try:
        obj.neighbourhood = request.POST['neighbourhood']
    except:
        pass
    try:
        f = request.POST['preapp']
        if f == 'on':
            obj.pre_approval = True
    except:
        pass
    try:
        obj.soon_looking_to_buy = request.POST['lookingtobuy']
    except:
        pass
    obj.selopt = 1
    obj.save()
    return redirect('/my_profile')

def form3(request):
    obj = profileModel.objects.get(user=request.user)
    obj.any_other = request.POST['any_other']
    try:
        a = request.POST['schools']
        if a == 'on':
            obj.schools = True
    except:
        obj.schools = False
    try:
        b = request.POST['commute']
        if b == 'on':
            obj.commute = True
    except:
        obj.commute = False
    try:
        c = request.POST['vastu']
        if c == 'on':
            obj.vastu = True
    except:
        obj.vastu = False
    try:
        d = request.POST['shop']
        if d == 'on':
            obj.shop = True
    except:
        obj.shop = False
    obj.selopt = 2
    obj.save()
    return redirect('/my_profile')

def form11(request):
    obj = profileModel.objects.get(pk=request.POST['id']).user
    obj.first_name = request.POST['name']
    obj.email = request.POST['email']
    obj.save()
    obj = profileModel.objects.get(user=obj)
    obj.phone = request.POST['phone']
    obj.occupation = request.POST['occupation']
    obj.selopt = 0
    obj.save()
    return redirect('/profile/'+obj.user.username)

def form21(request):
    obj = profileModel.objects.get(pk=request.POST['id'])
    try:
        a = request.POST['singlefamily']
        if a == 'on':
            obj.sf = True
    except:
        pass
    try:
        b = request.POST['townhome']
        if b == 'on':
            obj.th = True
    except:
        pass
    try:
        c = request.POST['condominium']
        if c == 'on':
            obj.cd = True
    except:
        pass
    try:
        d = request.POST['multifamily']
        if d == 'on':
            obj.mf = True
    except:
        pass
    try:
        e = request.POST['land']
        if e == 'on':
            obj.ln = True
    except:
        pass
    try:
        obj.minprice = request.POST['minprice']
    except:
        pass
    try:
        obj.maxprice = request.POST['maxprice']
    except:
        pass
    try:
        obj.stories = request.POST['stories']
    except:
        pass
    try:
        obj.minsqft = request.POST['minsqft']
    except:
        pass
    try:
        obj.maxsqft = request.POST['maxsqft']
    except:
        pass
    try:
        obj.minlot = request.POST['minlot']
    except:
        pass
    try:
        obj.maxlot = request.POST['maxlot']
    except:
        pass
    try:
        obj.beds = request.POST['beds']
    except:
        pass
    try:
        obj.bath = request.POST['bath']
    except:
        pass
    obj.selopt = 1
    obj.save()
    return redirect('/profile/'+obj.user.username)

def form31(request):
    obj = profileModel.objects.get(pk=request.POST['id'])
    obj.any_other = request.POST['any_other']
    try:
        a = request.POST['schools']
        if a == 'on':
            obj.schools = True
    except:
        pass
    try:
        b = request.POST['commute']
        if b == 'on':
            obj.commute = True
    except:
        pass
    try:
        c = request.POST['vastu']
        if c == 'on':
            obj.vastu = True
    except:
        pass
    try:
        d = request.POST['shop']
        if d == 'on':
            obj.shop = True
    except:
        pass
    obj.selopt = 2
    obj.save()
    return redirect('/profile/'+obj.user.username)

def home(request):
    if request.method == 'POST':
        a = request.POST['message']
        emailobj = EmailMessage(
            subject = 'Message recieved via website homepage',
            body = a,
            to = ['upclinch@gmail.com','khawarzia34@gmail.com']
        )
        emailobj.send()
    if request.user.is_authenticated:
        a = profileModel.objects.get(user=request.user)
        if a.Agent_or_Buyer == 'Agent':
            context = {'agentcheck':True}
            if a.is_master_agent:
                context['mastercheck'] = True
        else:
            context = {'agentcheck':False}
    else:
        context = {}
    return render(request, 'upclinch.html',context)


# ! USER PROFILE PAGE
@login_required
def myprofile(request):
    profile = profileModel.objects.get(user=request.user)
    if profile.approve == True:
        context = {
            'profile': profile,
            'section': 'dashboard'
        }
        if profile.Agent_or_Buyer == 'Buyer':
            context['agentcheck'] = False
            return render(request, 'page_47.html', context)
        if profile.Agent_or_Buyer == 'Agent':
            context['agentcheck'] = True
            if profile.is_master_agent:
                context['mastercheck'] = True
            return render(request, 'page_47.html', context)
    else:
        return redirect('/')


def contact(request):
    if request.method != 'POST':
        form = contactForm()
    else:
        form = contactForm(request.POST)
        if form.is_valid():
            mail_subject = 'Contact -- By -- ' + \
                form.cleaned_data.get('userName')
            to_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data.get('body')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('home')

    context = {'form': form}
    return render(request, 'mysite/contact.html', context)


# TODO  :   USER LOGIN VIEW
def login_user(request):
    context = {}
    try:
        a = request.GET['type']
        b = request.GET['proid']
        context['a'] = a
        context['b'] = b
    except:
        pass
    if request.method == 'POST':
        user = None
        for i in User.objects.all():
            if i.email == request.POST['username']:
                usrobj = i
                break
        try:
            user = authenticate(username=usrobj, password=request.POST['password'])
        except:
            pass
        if user is not None:
            login(request, user)
            try:
                a = request.POST['type']
                b = properties.objects.get(pk=int(request.POST['id']))
                if a == 'tour':
                    return redirect('/request-tour/0/'+str(b.id)+'/0')
                elif a == 'list':
                    return redirect('/property-detail/'+str(b.id)+'?action=openlist')
                elif a == 'offer':
                    return redirect('/property-detail/'+str(b.id)+'?action=openoffer')
                else:
                    return redirect(reverse("home"))
            except:
                return redirect(reverse("home"))
        else:
            messages.warning(
                request, 'Email or password may have been entered incorrectly.')
            return redirect('login')
    context['section'] = 'loginPage'
    return render(request, 'mysite/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


# TODO  :    USER REGISTRATION
def register_user(request):
    success_register = False
    try:
        a = request.GET['type']
        b = request.GET['id']
    except:
        a = ''
        b = ''
    if request.method != 'POST':
        form = registerForm()
        form_2 = profileInformFormRegister()
    else:
        form = registerForm(request.POST)
        if form.is_valid():
            userobj = User()
            userobj.username = str(len(User.objects.all()))+form.cleaned_data['name']
            userobj.first_name = form.cleaned_data['name']
            userobj.email = form.cleaned_data['email']
            userobj.save()
            userobj.set_password(form.cleaned_data['password2'])
            userobj.save()
            profile = profileModel()
            profile.user = userobj
            try:
                profile.phone = request.POST['phone']
            except:
                pass
            try:
                profile.occupation = request.POST['occupation']
            except:
                pass
            profile.save()
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request,user)
            try:
                c = request.POST['type']
                d = properties.objects.get(pk=int(request.POST['id']))
                if c == 'tour':
                    return redirect('/request-tour/0/'+str(d.id)+'/0')
                elif c == 'list':
                    return redirect('/property-detail/'+str(d.id)+'?action=openlist')
                elif c == 'offer':
                    return redirect('/property-detail/'+str(d.id)+'?action=openoffer')
                else:
                    pass
            except:
                pass
            success_register = True
            return render(request, 'mysite/register.html', {'form': form, 'section' : 'register', 'profile' : profile,'a':a,'b':b, "success_register" : success_register})
    return render(request, 'mysite/register.html', {'form': form, 'section' : 'register','a':a,'b':b})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.warning(request, 'User has been activated')
        return redirect('login')
    else:
        messages.warning(request, 'Invalid Activation Link')
        return redirect('register')

# @login_required
# def edit_profile(request):
#     try:
#         profile = profileModel.objects.get(user=request.user)
#     except:
#         profile=None
#     context={
#         'profile' : profile,
#         'section' : "editProfile"
#     }
#     return render(request, 'mysite/editProfile.html', context)


@login_required()
def edit_profile(request):
    if request.method != 'POST':
        form = EditProfileForm(instance=request.user)
    else:
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile has been updated.')
            # return redirect('home')
    try:
        profile = profileModel.objects.get(user=request.user)
    except:
        profile = profileModel.objects.create(user=request.user)
    if request.method != 'POST':
        if profile:
            form_2 = profileInformForm(instance=profile)
        else:
            form_2 = profileInformForm()
    else:
        if profile:
            form_2 = profileInformForm(request.POST, instance=profile)
        else:
            form_2 = profileInformForm(request.POST,)
        if form_2.is_valid():
            form_2.save()
            messages.success(request, 'Profile has been updated.')
            return redirect('home')

    try:
        profile = profileModel.objects.get(user=request.user)
    except:
        profile = None
    context = {
        'profile': profile,
        'section': "editProfile",
        'form': form,
        'form_2':form_2
    }
    return render(request, 'mysite/editProfile.html', context)


@login_required()
def edit_profile_user(request):
    try:
        profile = profileModel.objects.get(user=request.user)
    except:
        profile = profileModel.objects.create(user=request.user)
    if request.method != 'POST':
        if profile:
            form = profileInformForm(instance=profile)
        else:
            form = profileInformForm()
    else:
        if profile:
            form = profileInformForm(request.POST, instance=profile)
        else:
            form = profileInformForm(request.POST,)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been updated.')
            return redirect('home')
    try:
        profile = profileModel.objects.get(user=request.user)
    except:
        profile = None
    context = {
        'profile': profile,
        'section': "editProfile",
        'form': form
    }
    return render(request, 'mysite/editProfileUser.html', context)


@login_required()
def change_password(request):
    if request.method != 'POST':
        form = PasswordChangeForm(user=request.user)
    else:
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password has been updated.')
            return redirect('home')
    return render(request, 'mysite/change_password.html', {'form': form, 'section': "editProfile"})


@login_required
def changeopt(request,a):
    obj = profileModel.objects.get(user=request.user)
    obj.selopt = a
    obj.save()
    return redirect('/my_profile')