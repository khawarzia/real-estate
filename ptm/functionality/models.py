from django.db import models
from django.contrib.auth.models import User
from mysite.models import profileModel

CHOICES_TYPE=(
    ('In Creation','In Creation'),
    ('Requested','Requested'),
    ('Scheduled','Scheduled'),
    ('Cancelled','Cancelled'),
    ('Completed','Completed'),
)

class properties(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    city = models.CharField(max_length=100,blank=True)
    area = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=200,blank=True)
    price = models.IntegerField(default=0)
    sqft = models.FloatField(default=0)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    family_type = models.CharField(max_length=100,blank=True)
    year_built = models.IntegerField(default=2020)
    heating = models.CharField(max_length=100,blank=True)
    cooling = models.CharField(max_length=100,blank=True)
    parking = models.IntegerField(default=0)
    lot = models.IntegerField(default=0)
    description = models.TextField(max_length=2000,blank=True)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.user.username + ' has property worth ' + str(self.price))

class shortlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=100,blank=True)
    relproperties = models.ManyToManyField(properties,blank=True)
    note = models.TextField(max_length=2000,blank=True)
    shared_with = models.ForeignKey(User,on_delete=None,null=True,related_name='shared_with')
    linked_with = models.ForeignKey(User,on_delete=None,null=True,related_name='linked_with')

    def __str__(self):
        return (self.name)

    def sharepossible(self):
        if self.relproperties.count() > 0:
            return True
        else:
            return False
    
    def comprev(self):
        if self.relproperties.count() > 0:
            obj = profileModel.objects.get(user=self.user)
            if obj.Agent_or_Buyer == 'Agent':
                a = propertyrating.objects.filter(user=self.linked_with)
            else:
                a = propertyrating.objects.filter(user=self.user)
            b = []
            for i in self.relproperties.all():
                b.append(i)
            c = []
            for i in a:
                if (i.rating >= 0 and i.rating <= 2) and i.relproperty in self.relproperties.all():
                    c.append(i)
            if len(b) == len(c):
                return True
            else:
                return False
        else:
            return False

    def tourpossible(self):
        if self.relproperties.count() > 0:
            return True
        else:
            return False

class propertyrating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    relproperty = models.ForeignKey(properties,on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)

class notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='user')
    relproperty = models.ForeignKey(properties,on_delete=models.CASCADE,blank=True,related_name='relproperty')
    relshortlist = models.ForeignKey(shortlist,on_delete=models.CASCADE,null=True,related_name='relshortlist')
    note = models.TextField(max_length=2000,blank=True)

    def __str__(self):
        return (self.note)

class tourrequests(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='usertr')
    relproperty = models.ManyToManyField(properties,blank=True,related_name='relpropertytr')
    name = models.CharField(max_length=50)
    sel_date = models.CharField(max_length=200,blank=True)
    sel_time = models.CharField(max_length=200,blank=True)
    date1 = models.CharField(max_length=200,blank=True)
    time1_date1 = models.CharField(max_length=200,blank=True)
    time2_date1 = models.CharField(max_length=200,blank=True)
    time3_date1 = models.CharField(max_length=200,blank=True)
    date2 = models.CharField(max_length=200,blank=True)
    time1_date2 = models.CharField(max_length=200,blank=True)
    time2_date2 = models.CharField(max_length=200,blank=True)
    time3_date2 = models.CharField(max_length=200,blank=True)
    date3 = models.CharField(max_length=200,blank=True)
    time1_date3 = models.CharField(max_length=200,blank=True)
    time2_date3 = models.CharField(max_length=200,blank=True)
    time3_date3 = models.CharField(max_length=200,blank=True)
    status = models.CharField(max_length=20, blank=True, default='In Creation' ,choices=CHOICES_TYPE)
    note = models.TextField(max_length=1000,blank=True)
    linked_with = models.ForeignKey(User,null=True,on_delete=None,related_name='linked_withtr')
    shared_with = models.ForeignKey(User,null=True,on_delete=None,related_name='shared_withtr')

    def __str__(self):
        return (self.name + ' by ' + self.user.username + ' : ' + self.status)

    def vacant(self):
        return (8-self.relproperty.count())

    def statuscheck(self):
        if self.status == 'Completed' or self.status == 'Scheduled':
            return True
        else:
            return False
    
    def getdate(self):
        return self.sel_date

    def gettime(self):
        return self.sel_time


class tnotes(models.Model):
    relproperty = models.ForeignKey(properties,on_delete=models.CASCADE,blank=True,related_name='trelproperty')
    reltour = models.ForeignKey(tourrequests,on_delete=models.CASCADE,blank=True,related_name='treltour')
    note = models.TextField(max_length=2000,blank=True)

    def __str__(self):
        return (self.note)

class offers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    relproperty = models.ForeignKey(properties,on_delete=models.CASCADE,blank=True)
    note = models.CharField(max_length=200,blank=True)
    status = models.CharField(max_length=50,default='Requested')
    requested_date = models.CharField(max_length=200,blank=True)
    submitted_date = models.CharField(max_length=200,blank=True)
    contract_date = models.CharField(max_length=200,blank=True)
    fell_through_date = models.CharField(max_length=200,blank=True)
    closed_date = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.note

class agent_buyer(models.Model):
    agent = models.ForeignKey(User,on_delete=models.CASCADE,related_name='agent')
    buyers = models.ManyToManyField(User,related_name='buyers',blank=True)

    def __str__(self):
        return self.agent.username

    def get_for_temp(self):
        a = ''
        for i in self.buyers.all():
            a = a + str(i.username) + ','
        return a