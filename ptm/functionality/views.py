from django.shortcuts import render,redirect,HttpResponse
from .models import properties,shortlist,notes,tourrequests,offers,propertyrating,agent_buyer,tnotes
from .forms import propertyform
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from mysite.models import profileModel
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from Django_Project.settings import EMAIL_HOST_USER
import datetime

def search2(request):
    if request.method == 'POST':
        temp = datetime.datetime.now().strftime("%m/%d/%Y")
        offerobj = offers()
        offerobj.user = request.user
        offerobj.relproperty = properties.objects.get(pk=request.POST['id'])
        offerobj.note = request.POST['offer']
        offerobj.requested_date = temp
        offerobj.save()
    template = 'page_11.html'
    context = {}
    if request.user.is_authenticated:
        obj = profileModel.objects.get(user=request.user)
        if obj.Agent_or_Buyer == 'Agent':
            context['agentcheck'] = True
            if obj.is_master_agent:
                tempvar = []
                for i in agent_buyer.objects.all():
                    for j in i.buyers.all():
                        tempvar.append(j)
                context['listofbuyers'] = []
                for i in profileModel.objects.filter(Agent_or_Buyer = 'Buyer'):
                    if i.user not in tempvar:
                        context['listofbuyers'].append(i)
                context['mastercheck'] = True
            else:
                try:
                    obj2 = agent_buyer.objects.get(agent=obj.user)
                    buyerlist1 = obj2.buyers.all()
                    context['listofbuyers'] = []
                    for i in buyerlist1:
                        context['listofbuyers'].append(profileModel.objects.get(user=i))
                except:
                    obj2 = agent_buyer()
                    obj2.agent = obj.user
                    obj2.save()
                    context['listofbuyers'] = []
        else:
            context['agentcheck'] = False
    else:
        context['agentcheck'] = False
    probjs = []
    try:
        a = request.GET['city']
        context['searchquery'] = a
    except:
        context['listofproperty'] = probjs
        return render(request,template,context)
    objs = properties.objects.all()
    for i in objs:
        if a.lower() in i.city.lower():
            probjs.append(i)
    if request.user.is_authenticated:
        ratings = propertyrating.objects.filter(user=request.user)
        ratings1 = {}
        for i in probjs:
            a = propertyrating.objects.filter(relproperty=i)
            check = True
            for j in a:
                if j.user == request.user:
                    check = False
                    break
            if check:
                abcd = propertyrating()
                abcd.user = request.user
                abcd.relproperty = i
                abcd.save()
                check = True
        for i in ratings:
            if i.relproperty in probjs:
                ratings1[i.relproperty] = i.rating
        tours = tourrequests.objects.filter(user=request.user)
        tourdates = {}
        for i in tours:
            if i.status == 'Completed':
                tourdates[i] = i.sel_date
        context['ratings'] = ratings1
        context['tourdates'] = tourdates
        if context['agentcheck']:
            context['lists'] = [[],{}]
            context['tours'] = [[],{}]
            for i in shortlist.objects.all():
                if request.user == i.user:
                    if i.linked_with == None:
                        context['lists'][0].append(i)
                    else:
                        try:
                            context['lists'][1][i.linked_with].append(i)
                        except:
                            context['lists'][1][i.linked_with] = []
                            context['lists'][1][i.linked_with].append(i)
                elif request.user == i.shared_with:
                    try:
                        context['lists'][1][i.user].append(i)
                    except:
                        context['lists'][1][i.user] = []
                        context['lists'][1][i.user].append(i)
                else:
                    pass
            for i in tourrequests.objects.all():
                if request.user == i.user:
                    context['tours'][0].append(i)
                elif request.user == i.shared_with:
                    try:
                        context['tours'][1][i.user].append(i)
                    except:
                        context['tours'][1][i.user] = []
                        context['tours'][1][i.user].append(i)
                else:
                    pass
        else:
            context['lists'] = []
            context['tours'] = []
            for i in shortlist.objects.all():
                if i.user == request.user or i.shared_with == request.user:
                    context['lists'].append(i)
            for i in tourrequests.objects.all():
                if i.user == request.user or i.shared_with == request.user:
                    context['tours'].append(i)
    context['listofproperty'] = probjs
    try:
        a = request.POST['id']
        context['selectedprop'] = a
    except:
        context['selectedprop'] = '0'
    try:
        a = request.GET['check1']
        context['selectedprop'] = a
    except:
        context['selectedprop'] = '0'
    return render(request,template,context)

@login_required
def createproperty(request):
    template = 'new-property.html'
    form = propertyform(request.POST)
    if form.is_valid():
        a = form.cleaned_data
        b = properties()
        b.user = request.user
        b.price = a['price']
        b.sqft = a['sqft']
        b.beds = a['beds']
        b.baths = a['baths']
        b.family_type = a['family_type']
        b.year_built = a['year_built']
        b.heating = a['heating']
        b.cooling = a['cooling']
        b.parking = a['parking']
        b.lot = a['lot']
        b.description = a['description']
        b.save()
        try:
            image = a['image1']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            b.image1 = fs.url(filename)
            b.save()
            image = a['image2']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            b.image2 = fs.url(filename)
            b.save()
            image = a['image3']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            b.image3 = fs.url(filename)
            b.save()
            image = a['image4']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            b.image4 = fs.url(filename)
            b.save()
            image = a['image5']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            b.image5 = fs.url(filename)
            b.save()
        except:
            pass
    else:
        form = propertyform()
    context = {'form':form}
    return render(request,template,context)

def propertydetail(request,id):
    if request.method == 'POST':
        temp = datetime.datetime.now().strftime("%m/%d/%Y")
        a = offers()
        a.user = request.user
        a.relproperty = properties.objects.get(pk=id)
        a.note = request.POST['offer']
        a.requested_date = temp
        a.save()
    template = 'page_51.html'
    obj = properties.objects.get(pk=id)
    if request.user.is_authenticated:
        context = {'obj':obj}
        obj = profileModel.objects.get(user=request.user)
        if obj.Agent_or_Buyer == 'Agent':
            context['agentcheck'] = True
            if obj.is_master_agent:
                tempvar = []
                for i in agent_buyer.objects.all():
                    for j in i.buyers.all():
                        tempvar.append(j)
                context['listofbuyers'] = []
                for i in profileModel.objects.filter(Agent_or_Buyer = 'Buyer'):
                    if i.user not in tempvar:
                        context['listofbuyers'].append(i)
                context['mastercheck'] = True
            else:
                try:
                    obj2 = agent_buyer.objects.get(agent=obj.user)
                    buyerlist1 = obj2.buyers.all()
                    context['listofbuyers'] = []
                    for i in buyerlist1:
                        context['listofbuyers'].append(profileModel.objects.get(user=i))
                except:
                    obj2 = agent_buyer()
                    obj2.agent = obj.user
                    obj2.save()
                    context['listofbuyers'] = []
        else:
            context['agentcheck'] = False
            a = propertyrating.objects.filter(user=request.user)
            context['ratingyes'] = False
            for i in a:
                if i.relproperty.id == id and i.rating in [0,1,2]:
                    context['ratingyes'] = True
                    if i.rating == 0:
                        context['rating'] = 'fa-smile'
                    if i.rating == 1:
                        context['rating'] = 'fa-frown'
                    if i.rating == 2:
                        context['rating'] = 'fa-meh'
        if context['agentcheck']:
            context['lists'] = [[],{}]
            context['tours'] = [[],{}]
            for i in shortlist.objects.all():
                if request.user == i.user:
                    if i.linked_with == None:
                        context['lists'][0].append(i)
                    else:
                        try:
                            context['lists'][1][i.linked_with].append(i)
                        except:
                            context['lists'][1][i.linked_with] = []
                            context['lists'][1][i.linked_with].append(i)
                elif request.user == i.shared_with:
                    try:
                        context['lists'][1][i.user].append(i)
                    except:
                        context['lists'][1][i.user] = []
                        context['lists'][1][i.user].append(i)
                else:
                    pass
            for i in tourrequests.objects.all():
                if request.user == i.user:
                    context['tours'][0].append(i)
                elif request.user == i.shared_with:
                    try:
                        context['tours'][1][i.user].append(i)
                    except:
                        context['tours'][1][i.user] = []
                        context['tours'][1][i.user].append(i)
                else:
                    pass
        else:
            context['lists'] = []
            context['tours'] = []
            for i in shortlist.objects.all():
                if i.user == request.user or i.shared_with == request.user:
                    context['lists'].append(i)
            for i in tourrequests.objects.all():
                if i.user == request.user or i.shared_with == request.user:
                    context['tours'].append(i)
    else:
        context = {'obj':obj}
    try:
        context['action'] = request.GET['action']
    except:
        pass
    return render(request,template,context)

@login_required
def addtolist(request,listid,objid):
    listobj = shortlist.objects.get(pk=listid)
    obj = properties.objects.get(pk=objid)
    listobj.relproperties.add(obj)
    listobj.save()
    a = propertyrating.objects.get(user = request.user)
    for i in a:
        if i.relproperty == obj:
            break
        else:
            obj1 = propertyrating()
            obj1.user = request.user
            obj1.relproperty = obj
            obj1.save()
    return redirect('/property-detail/'+str(objid))

@login_required
def deletelist(request,id):
    listobj = shortlist.objects.get(pk=id)
    listobj.delete()
    return redirect('/manage-lists')

@login_required
def deletetour(request,id):
    tourobj = tourrequests.objects.get(pk=id)
    tourobj.delete()
    return redirect('/tour-requests')

@login_required
def removefromlist(request,listid,objid):
    listobj = shortlist.objects.get(pk=listid)
    obj = properties.objects.get(pk=objid)
    listobj.relproperties.remove(obj)
    listobj.save()
    return redirect('/show-list/'+str(listid))


# ! Interest List
@login_required
def managelists(request):
    if request.method == 'POST':
        a = request.POST
        obj = shortlist.objects.get(pk=a['id'])
        obj.name = a['listname']
        obj.save()
    template = 'page_24_End.html'
    lists = []
    check = 0
    obj = profileModel.objects.get(user=request.user)
    for i in shortlist.objects.all():
        if i.user == request.user or request.user == i.shared_with:
            if i.name or i.sharepossible():
                lists.append(i)
            else:
                if check >= 1:
                    i.delete()
                else:
                    check = check + 1
                    lists.append(i)
    for i in range(len(lists)-1):
        if lists[i].name == '':
            lists[i].delete()
    context = {'lists':reversed(lists)}
    context['agentlist'] = profileModel.objects.filter(Agent_or_Buyer = 'Agent')
    if obj.Agent_or_Buyer == 'Agent':
        context['agentcheck'] = True
        if obj.is_master_agent:
            tempvar = []
            for i in agent_buyer.objects.all():
                for j in i.buyers.all():
                    tempvar.append(j)
            context['buyerlist'] = []
            for i in profileModel.objects.filter(Agent_or_Buyer = 'Buyer'):
                if i.user not in tempvar:
                    context['buyerlist'].append(i)
            context['mastercheck'] = True
        else:
            try:
                obj2 = agent_buyer.objects.get(agent=obj.user)
                buyerlist1 = obj2.buyers.all()
                context['buyerlist'] = []
                for i in buyerlist1:
                    context['buyerlist'].append(profileModel.objects.get(user=i))
            except:
                obj2 = agent_buyer()
                obj2.agent = obj.user
                obj2.save()
                context['buyerlist'] = []
    else:
        context['agentcheck'] = False
    context['thisisuserpage'] = False
    return render(request,template,context)

@login_required
def createlist(request):
    obj = shortlist()
    obj.user = request.user
    obj.save()
    return redirect('/manage-lists')

@login_required
def createtour(request):
    obj = tourrequests()
    obj.user = request.user
    obj.save()
    return redirect('/tour-requests')

@login_required
def namelist(request,name,proid):
    obj = shortlist()
    obj.name = name
    obj.user = request.user
    obj.save()
    obj.relproperties.add(properties.objects.get(pk=proid))
    obj.save()
    return redirect('/manage-lists')

# ! Show Specific List View
@login_required
def showlist(request,id):
    template = 'page_30_End.html'
    obj = shortlist.objects.get(pk=id)
    if request.method == 'POST':
        a = request.POST['id']
        b = stripspace(request.POST['propertynote'])
        for i in notes.objects.all():
            if i.user == request.user and (i.relproperty == properties.objects.get(pk=a) and i.relshortlist == obj):
                i.delete()
                break
        note = notes()
        note.user = request.user
        note.relproperty = properties.objects.get(pk=a)
        note.relshortlist = obj
        note.note = b
        note.save()
    context = {'obj':obj}
    proobj = profileModel.objects.get(user=request.user)
    if proobj.Agent_or_Buyer == 'Agent':
        context['agentcheck'] = True
        if proobj.is_master_agent:
            tempvar = []
            for i in agent_buyer.objects.all():
                for j in i.buyers.all():
                    tempvar.append(j)
            context['buyerlist'] = []
            for i in profileModel.objects.filter(Agent_or_Buyer = 'Buyer'):
                if i.user not in tempvar:
                    context['buyerlist'].append(i)
            context['mastercheck'] = True
        else:
            try:
                obj2 = agent_buyer.objects.get(agent=proobj.user)
                buyerlist1 = obj2.buyers.all()
                context['buyerlist'] = []
                for i in buyerlist1:
                    context['buyerlist'].append(profileModel.objects.get(user=i))
            except:
                obj2 = agent_buyer()
                obj2.agent = proobj.user
                obj2.save()
                context['buyerlist'] = []
        context['lists'] = [[],{}]
        for i in shortlist.objects.all():
            if request.user == i.user:
                if i.linked_with == None:
                    context['lists'][0].append(i)
                else:
                    try:
                        context['lists'][1][i.linked_with].append(i)
                    except:
                        context['lists'][1][i.linked_with] = []
                        context['lists'][1][i.linked_with].append(i)
            elif request.user == i.shared_with:
                try:
                    context['lists'][1][i.user].append(i)
                except:
                    context['lists'][1][i.user] = []
                    context['lists'][1][i.user].append(i)
            else:
                pass
        context['agentlist'] = shortlist.objects.filter(user=request.user)
    else:
        context['agentcheck'] = False
        context['lists'] = []
        for i in shortlist.objects.all():
            if i.user == request.user or i.shared_with == request.user:
                context['lists'].append(i)
    objs = notes.objects.filter(relshortlist = obj)
    check = 2
    notelist = {}
    ratings = {}
    for i in obj.relproperties.all():
        if context['agentcheck']:
            ratings[i] = getrating(i,obj.linked_with)
        else:
            ratings[i] = getrating(i,request.user)
        for j in objs:
            if j.relproperty == i and j.relshortlist == obj:
                notelist[i] = j.note
                check = 1
                break
            else:
                check = 2
        if check == 2:
            notelist[i] = ''
    print(ratings)
    tours = tourrequests.objects.filter(user=request.user)
    tourdates = {}
    for i in tours:
        if i.status == 'Completed':
            tourdates[i] = i.sel_date
    context['notes'] = notelist.items()
    context['ratings'] = ratings.items()
    context['tourdates'] = tourdates.items()
    return render(request,template,context)


# ! Request A Tour Page
@login_required
def requesttour(request,listid,proid,reqid):
    context = {}
    context['props'] = []
    if request.method == 'POST':
        reqobj = tourrequests.objects.get(pk=request.POST['reqo'])
        a = request.POST.items()
        for i,j in a:
            if j == 'on':
                if reqobj.vacant() > 0:
                    reqobj.relproperty.add(properties.objects.get(pk=i))
                    reqobj.save()
                else:
                    break
        return redirect('/request-tour/0/0/'+str(reqobj.id))
    if (int(reqid) != 0):
        reqobj = tourrequests.objects.get(pk=reqid)
    elif (int(listid) == 0):
        obj = properties.objects.get(pk=proid)
        reqobj = tourrequests()
        reqobj.user = request.user
        temp = tourrequests.objects.filter(user=request.user)
        for i in temp:
            if i.name == '':
                i.delete()
        reqobj.name = request.user.get_full_name() + '_Tour_'+str(len(tourrequests.objects.filter(user=request.user)))
        reqobj.save()
        reqobj.relproperty.add(obj)
        reqobj.save()
        return redirect('/request-tour/0/0/'+str(reqobj.id))
    elif (int(proid) == 0):
        obj = shortlist.objects.get(pk=listid)
        reqobj = tourrequests()
        reqobj.user = request.user
        temp = tourrequests.objects.filter(user=request.user)
        for i in temp:
            if i.name == '':
                i.delete()
        reqobj.name = request.user.get_full_name() + '_Tour_'+str(len(tourrequests.objects.filter(user=request.user)))
        reqobj.save()
        for i in obj.relproperties.all():
            reqobj.relproperty.add(i)
        reqobj.save()
        return redirect('/request-tour/0/0/'+str(reqobj.id))
    else:
        pass
    try:
        a = request.GET['query']
        context['itissearched'] = True
        props = properties.objects.all()
        for i in props:
            if a.lower() in i.city.lower() and i not in reqobj.relproperty.all():
                context['props'].append(i)
    except:
        pass
    context['reqobj'] = reqobj
    ab = profileModel.objects.get(user=request.user)
    if ab.Agent_or_Buyer == 'Buyer':
        template = 'page_43_google_slides.html'
    else:
        if reqobj.status == 'Requested':
            template = 'page_99_googe_slide_req.html'
        else:
            template = 'page_99_googe_slide.html'
        if ab.is_master_agent:
            tempvar = []
            for i in agent_buyer.objects.all():
                for j in i.buyers.all():
                    tempvar.append(j)
            context['buyerlist'] = []
            for i in profileModel.objects.filter(Agent_or_Buyer = 'Buyer'):
                if i.user not in tempvar:
                    context['buyerlist'].append(i)
            context['mastercheck'] = True
        else:
            try:
                obj2 = agent_buyer.objects.get(agent=ab.user)
                buyerlist1 = obj2.buyers.all()
                context['buyerlist'] = []
                for i in buyerlist1:
                    context['buyerlist'].append(profileModel.objects.get(user=i))
            except:
                obj2 = agent_buyer()
                obj2.agent = ab.user
                obj2.save()
                context['buyerlist'] = []
    return render(request,template,context)

@login_required
def removefromtour(request,proid,reqid):
    obj = tourrequests.objects.get(pk=reqid)
    obj.relproperty.remove(properties.objects.get(pk=proid))
    return redirect('/request-tour/0/0/'+str(reqid))

@login_required
def submitrequest(request,reqid):
    try:
        reqobj = tourrequests.objects.get(pk=reqid)
    except:
        reqobj = tourrequests()
        reqobj.user = request.user
        reqobj.save()
    a = request.POST
    ab = profileModel.objects.get(user=request.user)
    if ab.Agent_or_Buyer == 'Agent':
        reqobj.sel_date = a['date1']
        reqobj.sel_time = a['time1'].strip()
        reqobj.name = a['tourname']
        reqobj.note = a['note']
        reqobj.status = a['status']
        reqobj.save()
        if a['linkedbuyernew']:
            b = User.objects.get(username=a['linkedbuyernew'])
            reqobj.linked_with = b
            if a['selection'] == 'send':
                if b != reqobj.user:
                    reqobj.shared_with = b
                    reqobj.status = 'Scheduled'
            else:
                pass
        else:
            if reqobj.linked_with:
                reqobj.linked_with = None
        reqobj.save()
    else:
        reqobj.date1 = a['date1']
        reqobj.time1_date1 = a['time1'].strip()
        reqobj.time2_date1 = a['time2'].strip()
        reqobj.time3_date1 = a['time3'].strip()
        reqobj.date2 = a['date2']
        reqobj.time1_date2 = a['time4'].strip()
        reqobj.time2_date2 = a['time5'].strip()
        reqobj.time3_date2 = a['time6'].strip()
        reqobj.date3 = a['date3']
        reqobj.time1_date3 = a['time7'].strip()
        reqobj.time2_date3 = a['time8'].strip()
        reqobj.time3_date3 = a['time9'].strip()
        reqobj.note = a['note']
        reqobj.name = a['tourname']
        reqobj.status = 'Requested'
        reqobj.linked_with = request.user
        reqobj.save()
        for i in agent_buyer.objects.all():
            if request.user in i.buyers.all():
                reqobj.shared_with = i.agent
                reqobj.save()
                return redirect('/show-tour/'+str(reqobj.id))
        objs = profileModel.objects.filter(is_master_agent = True)
        reqobj.shared_with = objs[0].user
        reqobj.save()
    return redirect('/show-tour/'+str(reqobj.id))

@login_required
def save_form_on_save(request):
    a = request.POST
    reqobj = tourrequests.objects.get(pk=a['id'])
    reqobj.date1 = a['date1']
    reqobj.time1_date1 = a['time1'].strip()
    reqobj.time2_date1 = a['time2'].strip()
    reqobj.time3_date1 = a['time3'].strip()
    reqobj.date2 = a['date2']
    reqobj.time1_date2 = a['time4'].strip()
    reqobj.time2_date2 = a['time5'].strip()
    reqobj.time3_date2 = a['time6'].strip()
    reqobj.date3 = a['date3']
    reqobj.time1_date3 = a['time7'].strip()
    reqobj.time2_date3 = a['time8'].strip()
    reqobj.time3_date3 = a['time9'].strip()
    reqobj.note = a['note']
    reqobj.name = a['tourname']
    reqobj.save()
    return HttpResponse('')

@login_required
def save_for_agent_tour(request):
    a = request.POST
    reqobj = tourrequests.objects.get(pk=a['id'])
    reqobj.sel_date = a['date1']
    reqobj.sel_time = a['time1'].strip()
    try:
        reqobj.name = a['tourname']
    except:
        pass
    reqobj.note = a['note']
    reqobj.status = a['status']
    reqobj.save()
    try:
        if a['linkedbuyernew']:
            b = User.objects.get(username=a['linkedbuyernew'])
            reqobj.linked_with = b
        else:
            if reqobj.linked_with:
                reqobj.linked_with = None
    except:
        pass
    reqobj.save()
    return HttpResponse('')

@login_required
def submitrequestagain(request,reqid):
    reqobj = tourrequests.objects.get(pk=reqid)
    reqobj.sel_date = request.POST['date1']
    reqobj.sel_time = request.POST['time1'].strip()
    reqobj.note = request.POST['note']
    reqobj.status = request.POST['status']
    reqobj.save()
    if request.POST['selection'] == 'send':
        reqobj.status = 'Scheduled'
        reqobj.save()
    return redirect('/tour-requests')


# ! SHOW TOUR VIEW
@login_required
def showtour(request,reqid):
    template = 'page_54_google_slides.html'
    context = {}
    context['props'] = []
    if request.method == 'POST':
        reqobj = tourrequests.objects.get(pk=request.POST['reqo'])
        a = request.POST.items()
        for i,j in a:
            if j == 'on':
                if reqobj.vacant() > 0:
                    reqobj.relproperty.add(properties.objects.get(pk=i))
                    reqobj.save()
                else:
                    break
        return redirect('/request-tour/0/0/'+str(reqobj.id))
    if (profileModel.objects.get(user=request.user).is_master_agent):
        context['agentcheck'] = True
        context['mastercheck'] = True
    elif (profileModel.objects.get(user=request.user).Agent_or_Buyer == 'Agent'):
        context['agentcheck'] = True
        context['mastercheck'] = False
    else:
        context['agentcheck'] = False
    reqobj = tourrequests.objects.get(pk=reqid)
    if reqobj.status == 'In Creation':
        return redirect('/request-tour/0/0/'+str(reqobj.id))
    if reqobj.status == 'Completed':
        template = 'complete-tour.html'
        objs = tnotes.objects.filter(reltour = reqobj)
        check = 2
        notelist = {}
        ratings = {}
        for i in reqobj.relproperty.all():
            if context['agentcheck']:
                ratings[i] = getrating(i,reqobj.linked_with)
            else:
                ratings[i] = getrating(i,request.user)
            for j in objs:
                if j.relproperty == i and j.reltour == reqobj:
                    notelist[i] = j.note
                    check = 1
                    break
                else:
                    check = 2
            if check == 2:
                notelist[i] = ''
        context['notes'] = notelist.items()
        context['ratings'] = ratings.items()
    try:
        a = request.GET['query']
        context['itissearched'] = True
        props = properties.objects.all()
        for i in props:
            if a.lower() in i.city.lower() and i not in reqobj.relproperty.all():
                context['props'].append(i)
    except:
        pass
    context['reqobj'] = reqobj
    if context['agentcheck']:
        if reqobj.status == 'Requested':
            template = 'page_99_googe_slide_req.html'
        elif reqobj.status == 'Completed':
            template = 'complete-tour.html'
        else:
            template = 'page_99_googe_slide.html'
            if context['mastercheck']:
                tempvar = []
                for i in agent_buyer.objects.all():
                    for j in i.buyers.all():
                        tempvar.append(j)
                context['buyerlist'] = []
                for i in profileModel.objects.filter(Agent_or_Buyer = 'Buyer'):
                    if i.user not in tempvar:
                        context['buyerlist'].append(i)
            else:
                try:
                    obj2 = agent_buyer.objects.get(agent=request.user)
                    buyerlist1 = obj2.buyers.all()
                    context['buyerlist'] = []
                    for i in buyerlist1:
                        context['buyerlist'].append(profileModel.objects.get(user=i))
                except:
                    obj2 = agent_buyer()
                    obj2.agent = request.user
                    obj2.save()
                    context['buyerlist'] = []
    return render(request,template,context)

@login_required
def addnote(request,id):
    template = 'add-note.html'
    context = {'id':id}
    if request.method == 'POST':
        id = request.POST['id']
        note1 = request.POST['note']
        for i in profileModel.objects.filter(Agent_or_Buyer = 'Agent'):
            a = notes()
            a.user = request.user
            a.reciever = i.user
            a.relproperty = properties.objects.get(pk=id)
            a.note = note1
            a.save()
        return redirect('/property-detail/'+str(id))
    return render(request,template,context)

# ! TOUR REQUEST PAGE
@login_required
def toursrequested(request):
    if request.method == 'POST':
        obj = tourrequests.objects.get(pk=request.POST['id'])
        obj.name = request.POST['listname']
        obj.save()
    template = 'tr.html'
    context = {}
    check = 0
    tours = []
    for i in tourrequests.objects.all():
        if i.user == request.user or request.user == i.shared_with:
            if i.name:
                tours.append(i)
            else:
                if check >= 1:
                    i.delete()
                else:
                    check = check + 1
                    tours.append(i)
    for i in range(len(tours)-1):
        if tours[i].name == '':
            tours[i].delete()
    context['objs'] = reversed(tours)
    a = profileModel.objects.get(user=request.user)
    if a.Agent_or_Buyer == 'Buyer':
        context['agentcheck'] = False
    else:
        context['agentcheck'] = True
        if a.is_master_agent:
            tempvar = []
            for i in agent_buyer.objects.all():
                for j in i.buyers.all():
                    tempvar.append(j)
            context['buyerlist'] = []
            for i in profileModel.objects.filter(Agent_or_Buyer = 'Buyer'):
                if i.user not in tempvar:
                    context['buyerlist'].append(i)
            context['mastercheck'] = True
        else:
            try:
                obj2 = agent_buyer.objects.get(agent=a.user)
                buyerlist1 = obj2.buyers.all()
                context['buyerlist'] = []
                for i in buyerlist1:
                    context['buyerlist'].append(profileModel.objects.get(user=i))
            except:
                obj2 = agent_buyer()
                obj2.agent = a.user
                obj2.save()
                context['buyerlist'] = []
    context['thisisuserpage'] = False
    return render(request,template,context)

@login_required
def shownotes(request):
    template = 'show-notes.html'
    context = {'sent':notes.objects.filter(user=request.user),'recieved':notes.objects.filter(reciever=request.user)}
    return render(request,template,context)

@login_required
def replytonote(request,id):
    template = 'add-note.html'
    context = {'id':id}
    if request.method == 'POST':
        id = request.POST['id']
        note1 = request.POST['note']
        noteobj = notes.objects.get(pk=id)
        a = notes()
        a.user = noteobj.reciever
        a.reciever = noteobj.user
        a.relproperty = noteobj.relproperty
        a.note = note1
        a.save()
        return redirect('/show-notes')
    return render(request,template,context)

@login_required
def listnotechange(request,id):
    obj = shortlist.objects.get(pk=id)
    obj.note = stripspace(request.POST['listnote'])
    obj.save()
    return redirect('/show-list/'+str(id))

@login_required
def addfromlist(request,listid,proid,currentid):
    obj1 = properties.objects.get(pk=proid)
    obj = shortlist.objects.get(pk=listid)
    obj.relproperties.add(obj1)
    obj.save()
    obj = shortlist.objects.get(pk=currentid)
    obj.relproperties.remove(obj1)
    obj.save()
    return redirect('/show-list/'+str(currentid))

@login_required
def listofbuyers(request):
    template = 'page_46_End.html'
    context = {}
    a = profileModel.objects.get(user=request.user)
    if a.Agent_or_Buyer != 'Agent':
        return redirect('/')
    else:
        context['agentcheck'] = True
        if a.is_master_agent:
            tempvar = []
            for i in agent_buyer.objects.all():
                for j in i.buyers.all():
                    tempvar.append(j)
            context['objs'] = []
            for i in profileModel.objects.filter(Agent_or_Buyer = 'Buyer'):
                if i.user not in tempvar:
                    context['objs'].append(i)
            context['mastercheck'] = True
        else:
            try:
                obj2 = agent_buyer.objects.get(agent=a.user)
                buyerlist1 = obj2.buyers.all()
                context['objs'] = []
                for i in buyerlist1:
                    context['objs'].append(profileModel.objects.get(user=i))
            except:
                obj2 = agent_buyer()
                obj2.agent = a.user
                obj2.save()
                context['objs'] = []
    return render(request,template,context)

@login_required
def addtotour(request,tid,proid):
    obj = tourrequests.objects.get(pk=tid)
    obj.relproperty.add(properties.objects.get(pk=proid))
    obj.save()
    return redirect('/request-tour/0/0/'+str(tid))

@login_required
def approvetour(request,id):
    obj = tourrequests.objects.get(pk=id)
    obj.status = 'Scheduled'
    obj.save()
    return redirect('/show-tour/'+str(id))

@login_required
def canceltour(request,id):
    obj = tourrequests.objects.get(pk=id)
    obj.status = 'Cancelled'
    obj.save()
    return redirect('/show-tour/'+str(id))

@login_required
def offer(request,id):
    temp = datetime.datetime.now().strftime("%m/%d/%Y")
    obj = offers()
    obj.user = request.user
    obj.relproperty = properties.objects.get(pk=id)
    obj.note = request.POST['offer']
    obj.requested_date = temp
    obj.save()
    return redirect('/property-detail/'+str(id))

@login_required
def offer_from_list(request,id):
    temp = datetime.datetime.now().strftime("%m/%d/%Y")
    obj = offers()
    obj.user = request.user
    obj.relproperty = properties.objects.get(pk=request.POST['id'])
    obj.note = request.POST['offer']
    obj.requested_date = temp
    obj.save()
    return redirect('/show-list/'+str(id))


# ! AGENT OFFERS VIEW
@login_required
def agent_offercheck(request):
    context = {}
    if (profileModel.objects.get(user=request.user).Agent_or_Buyer == 'Agent'):
        template = 'page_80_End.html'
        objs = offers.objects.all()
        context['agentcheck'] = True
        if (profileModel.objects.get(user=request.user).is_master_agent):
            context['mastercheck'] = True
    else:
        template = 'page_43.html'
        objs = offers.objects.filter(user=request.user)
        context['ic'] = []
        context['req'] = []
        context['sub'] = []
        context['ft'] = []
        context['cl'] = []
        for i in objs:
            if i.status == 'In Contract':
                context['ic'].append(i)
            if i.status == 'Requested':
                context['req'].append(i)
            if i.status == 'Submitted':
                context['sub'].append(i)
            if i.status == 'Fell Through':
                context['ft'].append(i)
            if i.status == 'Closed':
                context['cl'].append(i)
        context['agentcheck'] = False
    context['offers'] = objs
    return render(request,template,context)

@login_required
def tour(request,id):
    obj = tourrequests()
    obj.user = request.user
    obj.name = request.POST['tourname']
    obj.save()
    obj.relproperty.add(properties.objects.get(pk=id))
    obj.save()
    return redirect('/property-detail/'+str(id))

@login_required
def changeofferstatus(request):
    a = request.POST
    obj = offers.objects.get(pk=a['id'])
    temp = obj.status
    if a['offer_status'] == 'Requested':
        obj.requested_date = a['date']
    elif a['offer_status'] == 'Submitted':
        obj.submitted_date = a['date']
    elif a['offer_status'] == 'In Contract':
        obj.contract_date = a['date']
    elif a['offer_status'] == 'Fell Through':
        obj.fell_through_date = a['date']
    else:
        obj.closed_date = a['date']
    obj.status = a['offer_status']
    obj.save()
    if temp == 'Requested':
        a = 1
    elif temp == 'Submitted':
        a = 2
    elif temp == 'In Contract':
        a = 3
    elif temp == 'Fell Through':
        a = 4
    else:
        a = 5
    return redirect('/detail-offer/'+str(a))


# ! SPECIFIC BUYER PROFILE PAGE
@login_required
def profilepage(request,usr):
    if request.user.username == usr:
        return redirect('/')
    template = 'page_471.html'
    objs = profileModel.objects.all()
    obj = None
    for i in objs:
        if i.user.username == usr:
            obj = i
            break
    context = {}
    context['agentcheck'] = True
    context['obj'] = obj
    return render(request,template,context)

@login_required
def sharelist(request,usr,id):
    obj = shortlist.objects.get(pk=id)
    a = User.objects.get(username=usr)
    obj.shared_with = a
    obj.save()
    email = EmailMessage(
        subject = request.user.username + ' shared an Interest list',
        body = request.get_host()+'/show-list/'+str(id)+' is the link to the list.',
        to = [a.email]
    )
    email.send()
    return

@login_required
def sharelistbuyer(request,id):
    obj = shortlist.objects.get(pk=id)
    for i in agent_buyer.objects.all():
        if request.user in i.buyers.all():
            obj.linked_with = obj.user
            obj.shared_with = i.agent
            obj.save()
            return
    objs = profileModel.objects.filter(is_master_agent=True)
    if profileModel.objects.get(user=obj.user).Agent_or_Buyer != 'Agent':
        obj.linked_with = obj.user
        obj.shared_with = objs[0].user
    else:
        pass
    obj.save()
    return

@login_required
def unlinklist(request,id):
    obj = shortlist.objects.get(pk=id)
    for i in obj.shared_with.all():
        obj.shared_with.remove(i)
    obj.save()
    return

@login_required
def ratepro(request,listid,proid,rating):
    objp = properties.objects.get(pk=proid)
    for i in propertyrating.objects.all():
        if objp == i.relproperty and i.user == request.user:
            if rating == i.rating:
                i.rating = 3
            else:
                i.rating = rating
            i.save()
            return redirect('/show-list/'+str(listid))
    obj = propertyrating()
    obj.user = request.user
    obj.relproperty = objp
    obj.rating = rating
    obj.save()
    return redirect('/show-list/'+str(listid))

@login_required
def rateprot(request,listid,proid,rating):
    objp = properties.objects.get(pk=proid)
    for i in propertyrating.objects.all():
        if objp == i.relproperty and i.user == request.user:
            if rating == i.rating:
                i.rating = 3
            else:
                i.rating = rating
            i.save()
            return redirect('/show-tour/'+str(listid))
    obj = propertyrating()
    obj.user = request.user
    obj.relproperty = objp
    obj.rating = rating
    obj.save()
    return redirect('/show-tour/'+str(listid))

@login_required
def reactive(request,id):
    obj = tourrequests.objects.get(pk=id)
    obj.status = 'Requested'
    obj.save()
    return redirect('/show-tour/'+str(id))


# ! BUYER DETAIL OFFER
@login_required
def detailoffer(request,sel):
    template = 'page_81_End.html'
    context = {}
    if sel == 1:
        context['title'] = 'Requested'
        objs = offers.objects.filter(status='Requested')
    elif sel == 2:
        context['title'] = 'Submitted'
        objs = offers.objects.filter(status='Submitted')
    elif sel == 3:
        context['title'] = 'In Contract'
        objs = offers.objects.filter(status='In Contract')
    elif sel == 4:
        context['title'] = 'Fell Through'
        objs = offers.objects.filter(status='Fell Through')
    else:
        context['title'] = 'Closed'
        objs = offers.objects.filter(status='Closed')
    context['data'] = {}
    check = True
    context['agentcheck'] = True
    try:
        obj = agent_buyer.objects.get(agent=request.user)
        for i in obj.buyers.all():
            context['data'][i.get_full_name() + ': ' + i.email] = []
            check = False
    except:
        if profileModel.objects.get(user=request.user).is_master_agent:
            tempvar = []
            for i in agent_buyer.objects.all():
                for j in i.buyers.all():
                    tempvar.append(j)
            for i in profileModel.objects.filter(Agent_or_Buyer='Buyer'):
                if i.user not in tempvar:
                    context['data'][i.user.get_full_name() + ': ' + i.user.email] = []
                check = False
    if check:
        return render(request,template,context)
    for i in objs:
        try:
            context['data'][i.user.get_full_name() + ': ' + i.user.email].append(i)
        except:
            pass
    return render(request,template,context)

@login_required
def changelinked(request,id,usr):
    obj = shortlist.objects.get(pk=id)
    obj.linked_with = User.objects.get(username=usr)
    obj.save()
    return

@login_required
def removelinked(request,id):
    obj = shortlist.objects.get(pk=id)
    obj.linked_with = None
    obj.save()
    return

@login_required
def clonelist(request,id):
    obj = shortlist.objects.get(pk=id)
    newobj = shortlist()
    newobj.user = request.user
    newobj.name = 'Copy of '+obj.name
    newobj.save()
    for i in obj.relproperties.all():
        newobj.relproperties.add(i)
    newobj.save()
    return redirect('/manage-lists')

@login_required
def sharelistfinal(request,id):
    obj = shortlist.objects.get(pk=id)
    if obj.user != obj.linked_with:
        obj.shared_with = obj.linked_with
    else:
        pass
    obj.save()
    return redirect('/manage-lists')

@login_required
def linkunlinklist(request,id):
    obj = shortlist.objects.get(pk=id)
    obj.linked_with = None
    obj.save()
    return redirect('/show-list/'+str(id))

@login_required
def newlistsearch(request,proid,listname):
    obj = shortlist()
    obj.user = request.user
    if listname == 'nonenone':
        temp = shortlist.objects.filter(user=request.user)
        for i in temp:
            if i.name == '':
                i.delete()
        obj.name = request.user.get_full_name() + '_List_'+str(len(shortlist.objects.filter(user=request.user)))
    else:
        obj.name = listname
    obj.save()
    obj.relproperties.add(properties.objects.get(pk=proid))
    obj.save()
    return redirect('/property-detail/'+str(proid))

@login_required
def newlistsearchagent(request,proid,listname,buyer):
    obj = shortlist()
    obj.user = request.user
    if listname == 'nonenone':
        temp = shortlist.objects.filter(user=request.user)
        for i in temp:
            if i.name == '':
                i.delete()
        obj.name = request.user.get_full_name() + '_List_'+str(len(shortlist.objects.filter(user=request.user)))
    else:
        obj.name = listname
    try:
        obj.linked_with = User.objects.get(first_name=buyer)
    except:
        pass
    obj.save()
    obj.relproperties.add(properties.objects.get(pk=proid))
    obj.save()
    return redirect('/property-detail/'+str(proid))


# ! SPECIFIC USER  DETAILS
@login_required
def userlists(request,usr):
    userobj = User.objects.get(username=usr)
    if request.method == 'POST':
        a = request.POST
        obj = shortlist.objects.get(pk=a['id'])
        obj.name = a['listname']
        obj.save()
    template = 'page_24_End.html'
    lists = []
    check = 0
    for i in shortlist.objects.all():
        if i.user == request.user:
            if i.shared_with == userobj or i.linked_with == userobj:
                if i.name and i.sharepossible():
                    if i not in lists:
                        lists.append(i)
        if i.user == userobj:
            if i.shared_with == request.user or i.linked_with == request.user:
                if i.name and i.sharepossible():
                    if i not in lists:
                        lists.append(i)
    for i in range(len(lists)-1):
        if lists[i].name == '':
            lists[i].delete()
    context = {'lists':reversed(lists)}
    context['agentlist'] = profileModel.objects.filter(Agent_or_Buyer = 'Agent')
    a = profileModel.objects.get(user=request.user)
    if a.is_master_agent:
        tempvar = []
        for i in agent_buyer.objects.all():
            for j in i.buyers.all():
                tempvar.append(j)
        context['buyerlist'] = []
        for i in profileModel.objects.filter(Agent_or_Buyer = 'Buyer'):
            if i.user not in tempvar:
                context['buyerlist'].append(i)
        context['mastercheck'] = True
    else:
        try:
            obj2 = agent_buyer.objects.get(agent=a.user)
            buyerlist1 = obj2.buyers.all()
            context['buyerlist'] = []
            for i in buyerlist1:
                context['buyerlist'].append(profileModel.objects.get(user=i))
        except:
            obj2 = agent_buyer()
            obj2.agent = a.user
            obj2.save()
            context['buyerlist'] = []
    context['agentcheck'] = True
    context['thisisuserpage'] = True
    context['userobj'] = userobj
    return render(request,template,context)

@login_required
def usertours(request,usr):
    if request.method == 'POST':
        obj = tourrequests.objects.get(pk=request.POST['id'])
        obj.name = request.POST['listname']
        obj.save()
    template = 'tr.html'
    context = {}
    context['agentcheck'] = True
    userobj = User.objects.get(username=usr)
    objs = tourrequests.objects.all()
    tobjs = []
    check = 0
    for i in objs:
        if i.user == request.user:
            if i.shared_with == userobj or i.linked_with == userobj:
                if i.name and i.relproperty.count() > 0:
                    if i not in tobjs:
                        tobjs.append(i)
        if i.user == userobj:
            if i.shared_with == request.user or i.linked_with == request.user:
                if i.name and i.relproperty.count() > 0:
                    if i not in tobjs:
                        tobjs.append(i)
    for i in range(len(tobjs)-1):
        if tobjs[i].name == '':
            tobjs[i].delete()
    context['objs'] = reversed(tobjs)
    context['thisisuserpage'] = True
    context['userobj'] = userobj
    return render(request,template,context)

@login_required
def changelinkedtour(request,id,usr):
    obj = tourrequests.objects.get(pk=id)
    obj.linked_with = User.objects.get(username=usr)
    obj.save()
    return

@login_required
def clonetour(request,id):
    obj = tourrequests.objects.get(pk=id)
    newobj = tourrequests()
    newobj.user = request.user
    newobj.name = 'Copy of '+obj.name
    newobj.date1 = obj.date1
    newobj.date2 = obj.date2
    newobj.date3 = obj.date3
    newobj.time1_date1 = obj.time1_date1
    newobj.time2_date1 = obj.time2_date1
    newobj.time3_date1 = obj.time3_date2
    newobj.time1_date2 = obj.time1_date2
    newobj.time2_date2 = obj.time2_date2
    newobj.time3_date2 = obj.time3_date2
    newobj.time1_date3 = obj.time1_date3
    newobj.time2_date3 = obj.time2_date3
    newobj.time3_date3 = obj.time3_date3
    newobj.note = obj.note
    newobj.save()
    for i in obj.relproperty.all():
        newobj.relproperty.add(i)
    newobj.save()
    return redirect('/tour-requests')

@login_required
def removelinkedtour(request,id):
    obj = tourrequests.objects.get(pk=id)
    obj.linked_with = None
    obj.save()
    return

@login_required
def listforbuyer(request,usr):
    userobjs = User.objects.all()
    for i in userobjs:
        if i.username == usr:
            userobj = i
            break
    obj = shortlist()
    obj.user = request.user
    obj.linked_with = userobj
    obj.save()
    return redirect('/user-lists/'+usr)

@login_required
def tourforbuyer(request,usr):
    userobjs = User.objects.all()
    for i in userobjs:
        if i.username == usr:
            userobj = i
            break
    obj = tourrequests()
    obj.user = request.user
    obj.linked_with = userobj
    obj.save()
    return redirect('/user-tours/'+usr)

@login_required
def buyerofferspec(request,usr):
    context = {}
    context['agentcheck'] = True
    template = 'page_43.html'
    userobjs = User.objects.all()
    for i in userobjs:
        if i.username == usr:
            userobj = i
            break
    context['userobj'] = userobj
    objs = offers.objects.filter(user=userobj)
    context['ic'] = []
    context['req'] = []
    context['sub'] = []
    context['ft'] = []
    context['cl'] = []
    for i in objs:
        if i.status == 'In Contract':
            context['ic'].append(i)
        if i.status == 'Requested':
            context['req'].append(i)
        if i.status == 'Submitted':
            context['sub'].append(i)
        if i.status == 'Fell Through':
            context['ft'].append(i)
        if i.status == 'Closed':
            context['cl'].append(i)
    context['thisisuserpage'] = True
    return render(request,template,context)

@login_required
def canceltouragent(request,id):
    obj = tourrequests.objects.get(pk=id)
    obj.status = 'Cancelled'
    obj.save()
    return redirect('/show-tour/'+str(id))

@login_required
def movelistpro(request,listid,proid):
    a = request.POST['listname']
    b = request.POST['buyername']
    obj = shortlist()
    obj.user = request.user
    if a == '':
        temp = shortlist.objects.filter(user=request.user)
        for i in temp:
            if i.name == '':
                i.delete()
        obj.name = request.user.get_full_name() + '_List_'+str(len(shortlist.objects.filter(user=request.user)))
    else:
        obj.name = a
    if b != '':
        c = User.objects.get(first_name=b)
        obj.linked_with = c
    else:
        pass
    obj.save()
    probj = properties.objects.get(pk=proid)
    obj.relproperties.add(probj)
    obj.save()
    obj2 = shortlist.objects.get(pk=listid)
    obj2.relproperties.remove(probj)
    obj2.save()
    return redirect('/manage-lists')

@login_required
def movelistprobuyer(request,listid,proid):
    a = request.POST['listname']
    obj = shortlist()
    obj.user = request.user
    if a == '':
        temp = shortlist.objects.filter(user=request.user)
        for i in temp:
            if i.name == '':
                i.delete()
        obj.name = request.user.get_full_name() + '_List_'+str(len(shortlist.objects.filter(user=request.user)))
    else:
        obj.name = a
    obj.save()
    probj = properties.objects.get(pk=proid)
    obj.relproperties.add(probj)
    obj.save()
    obj2 = shortlist.objects.get(pk=listid)
    obj2.relproperties.remove(probj)
    obj2.save()
    return redirect('/manage-lists')

@login_required
def changedateoffer(request,date1,date2,date3,id):
    obj = offers.objects.get(pk=id)
    temp = str(date3)+'-'+str(date1)+'-'+str(date2)
    if obj.status == 'Requested':
        obj.requested_date = temp
    elif obj.status == 'Submitted':
        obj.submitted_date = temp
    elif obj.status == 'In Contract':
        obj.contract_date = temp
    elif obj.status == 'Fell Through':
        obj.fell_through_date = temp
    else:
        obj.closed_date = temp
    obj.save()
    return

def agent_buyer_relation(request):
    template = 'agent_buyer.html'
    context = {}
    objs = agent_buyer.objects.all()
    context['objs'] = objs
    context['agentcheck'] = True
    context['mastercheck'] = True
    return render(request,template,context)

def new_relation(request):
    template = 'new-relation.html'
    context = {}
    if request.method == 'POST':
        obj = agent_buyer()
        obj.agent = User.objects.get(username=request.POST['agent_name'])
        obj.save()
        try:
            a = request.POST['buyers'].split(',')
            for i in a:
                userobj = User.objects.get(username=i)
                obj.buyers.add(userobj)
                obj.save()
                obj1 = shortlist.objects.filter(user=userobj)
                for j in obj1:
                    if j.shared_with:
                        j.shared_with = obj.agent
                        j.linked_with = j.user
                        j.save()
                obj1 = tourrequests.objects.filter(user=userobj)
                for j in obj1:
                    if j.shared_with:
                        j.shared_with = obj.agent
                        j.linked_with = j.user
                        j.save()
            for i in agent_buyer.objects.all():
                if i == obj:
                    continue
                else:
                    pass
                for j in request.POST['buyers']:
                    if j in i.buyers.all():
                        i.buyers.remove(j)
                        i.save()
        except:
            pass
        return redirect('/agent-buyer-relation')
    objs = profileModel.objects.all()
    obja = []
    objb = []
    for i in objs:
        if i.Agent_or_Buyer == 'Buyer':
            objb.append(i)
        if i.Agent_or_Buyer == 'Agent' and i.is_master_agent == False:
            try:
                print(agent_buyer.objects.get(agent=i.user))
            except:
                obja.append(i)
    context['obja'] = obja
    context['objb'] = objb
    context['agentcheck'] = True
    context['mastercheck'] = True
    return render(request,template,context)

def delete_rel(request,id):
    obj = agent_buyer.objects.get(pk=id)
    obj.delete()
    return redirect('/agent-buyer-relation')

def edit_rel(request,id):
    template = 'edit-relation.html'
    context = {}
    obj = agent_buyer.objects.get(pk=id)
    if request.method == 'POST':
        obj.agent = User.objects.get(username=request.POST['agent_name'])
        obj.save()
        for i in obj.buyers.all():
            obj.buyers.remove(i)
            obj.save()
        try:
            a = request.POST['buyers'].split(',')
            for i in a:
                userobj = User.objects.get(username=i)
                obj.buyers.add(userobj)
                obj.save()
                obj1 = shortlist.objects.filter(user=userobj)
                for j in obj1:
                    if j.shared_with:
                        j.shared_with = obj.agent
                        j.linked_with = j.user
                        j.save()
                obj1 = tourrequests.objects.filter(user=userobj)
                for j in obj1:
                    if j.shared_with:
                        j.shared_with = obj.agent
                        j.linked_with = j.user
                        j.save()
            for i in agent_buyer.objects.all():
                if i == obj:
                    continue
                else:
                    pass
                for j in request.POST['buyers']:
                    if j in i.buyers.all():
                        i.buyers.remove(j)
                        i.save()
        except:
            pass
        return redirect('/agent-buyer-relation')
    context['obj'] = obj
    objs = profileModel.objects.all()
    obja = []
    objb = []
    for i in objs:
        if i.Agent_or_Buyer == 'Buyer':
            objb.append(i)
        if i.Agent_or_Buyer == 'Agent' and i.is_master_agent == False:
            try:
                print(agent_buyer.objects.get(agent=i.user))
            except:
                obja.append(i)
    context['obja'] = obja
    context['objb'] = objb
    context['agentcheck'] = True
    context['mastercheck'] = True
    return render(request,template,context)

def get_tour_date(request,id):
    objs = tourrequests.objects.filter(user=request.user)
    obj = properties.objects.get(pk=id)
    for i in objs:
        if i.status == 'Completed' and obj in i.relproperties.all():
            return HttpResponse(i.sel_date)
    return HttpResponse('none')

def get_offer_date(request,id):
    objs = offers.objects.filter(user=request.user)
    for i in objs:
        if i.relproperty.id == id:
            return HttpResponse(i.requested_date)
    return HttpResponse('none')

def testing(request):
    template = 'test.html'
    context = {}
    return render(request,template,context)

def testing1(request):
    return HttpResponse(request.user.username)

def submittournote(request,id):
    obj = tourrequests.objects.get(pk=id)
    obj.note = request.POST['listnote']
    obj.save()
    return redirect('/show-tour/'+str(id))

def tournote(request,id,reqid):
    objs = tnotes.objects.all()
    a = None
    for i in objs:
        if i.relproperty.id == id and i.reltour.id == reqid:
            a = i
            break
    if a == None:
        obj = tnotes()
        obj.relproperty = properties.objects.get(pk=id)
        obj.reltour = tourrequests.objects.get(pk=reqid)
    else:
        obj = a
    obj.note = request.POST['propertynote']
    obj.save()
    return redirect('/show-tour/'+str(reqid))

def rerequesttour(request,id):
    obj = tourrequests.objects.get(pk=id)
    obj.status = 'In Creation'
    obj.date1 = ''
    obj.time1_date1 = ''
    obj.time2_date1 = ''
    obj.time3_date1 = ''
    obj.date2 = ''
    obj.time1_date2 = ''
    obj.time2_date2 = ''
    obj.time3_date2 = ''
    obj.date3 = ''
    obj.time1_date3 = ''
    obj.time2_date3 = ''
    obj.time3_date3 = ''
    obj.save()
    return redirect('/show-tour/'+str(id))

def clonetour2(request,id):
    obj = tourrequests.objects.get(pk=id)
    obj2 = tourrequests()
    obj2.user = obj.user
    obj2.name = 'Copy of '+obj.name
    obj2.save()
    for i in obj.relproperty.all():
        obj2.relproperty.add(i)
    obj2.save()
    return redirect('/show-tour/'+str(obj2.id))
    













#helping functions
def stripspace(a):
    b = ''
    check = 1
    for i in a:
        if check == 1:
            if i == ' ':
                continue
            elif i == '\n':
                continue
            else:
                check = 2
        if check == 2:
            b = b + i
    return b

def getrating(a,b):
    for i in propertyrating.objects.all():
        if i.user == b and i.relproperty == a:
            return i.rating