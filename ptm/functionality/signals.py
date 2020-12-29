from django.db.models.signals import m2m_changed
from .models import agent_buyer,shortlist,tourrequests
from mysite.models import profileModel
from django.dispatch import receiver

def savefunc(sender,instance,**kwargs):
    obj = profileModel.objects.get(user=instance.agent)
    print(obj)
    if obj.Agent_or_Buyer == 'Buyer':
        instance.delete()
    else:
        pass
    buyers = instance.buyers.all()
    for i in buyers:
        obj = profileModel.objects.get(user=i)
        if obj.Agent_or_Buyer == 'Buyer':
            obj1 = shortlist.objects.filter(user=i)
            for j in obj1:
                if j.shared_with:
                    j.shared_with = instance.agent
                    j.linked_with = j.user
                    j.save()
            obj1 = tourrequests.objects.filter(user=i)
            for j in obj1:
                if j.shared_with:
                    j.shared_with = instance.agent
                    j.linked_with = j.user
                    j.save()
        else:
            instance.buyers.remove(i)
            instance.save()
    return

