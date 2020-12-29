from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

CHOICES_TYPE = (
    ('Buyer', 'Buyer'),
    ('Agent', 'Agent')
)

choice1 =(('Short Commute to work','Short Commute to work'),
          ('Access to shopping','Access to shopping'),
          ('Vastu Preference','Vastu Preference'),
          ('School Requirements','School Requirements'),
           )


class profileModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    approve = models.BooleanField(default=True)
    Agent_or_Buyer = models.CharField(max_length=10, blank=True, default='Buyer' ,choices=CHOICES_TYPE)
    is_master_agent = models.BooleanField(default=False)
    phone=models.CharField(max_length=11,blank=True, default='')
    occupation=models.CharField(max_length=200,blank=True, default='')
    #Property Requirements
    minprice = models.CharField(max_length=200,blank=True,default=' ')
    maxprice = models.CharField(max_length=200,blank=True,default=' ')
    minsqft = models.CharField(max_length=200,blank=True,default=' ')
    maxsqft = models.CharField(max_length=200,blank=True,default=' ')
    beds=models.CharField(max_length=200,blank=True,default='1')
    bath=models.CharField(max_length=200,blank=True,default='1')
    minlot = models.CharField(max_length=200,blank=True,default=' ')
    maxlot = models.CharField(max_length=200,blank=True,default=' ')
    stories=models.CharField(max_length=200,blank=True,default=' ')
    any_other = models.CharField(max_length=200,blank=True,default=' ')
    date = models.DateTimeField(auto_now_add=True)
    sf = models.BooleanField(default=False)
    th = models.BooleanField(default=False)
    cd = models.BooleanField(default=False)
    mf = models.BooleanField(default=False)
    ln = models.BooleanField(default=False)
    schools = models.BooleanField(default=False)
    commute = models.BooleanField(default=False)
    vastu = models.BooleanField(default=False)
    shop = models.BooleanField(default=False)
    neighbourhood = models.CharField(max_length=200,blank=True)
    pre_approval = models.BooleanField(default=False)
    soon_looking_to_buy = models.CharField(max_length=200,null=True,blank=True)
    selopt = models.IntegerField(default=0)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
