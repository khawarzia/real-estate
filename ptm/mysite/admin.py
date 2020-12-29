


from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import *
from functionality.models import *


class MyAdminSite(AdminSite):
    site_header = 'Real Estate'
    site_title  = 'Real Estate'
    index_title = 'Real Estate'
    # You can add on more attributes if you need 
    # Check out https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#adminsite-objects

# Create admin_site object from MyAdminSite
my_admin_site = MyAdminSite(name='Real Estate')



# Create and register all of your models
# ....

# This is the default Django Contrib Admin user / group object
# Add this if you need to edit the users / groups in your custom admin
my_admin_site.register(Group, GroupAdmin)
my_admin_site.register(User, UserAdmin)
my_admin_site.register(profileModel)
my_admin_site.register(properties)
my_admin_site.register(notes)
my_admin_site.register(shortlist)
my_admin_site.register(tourrequests)
my_admin_site.register(offers)
my_admin_site.register(propertyrating)
my_admin_site.register(tnotes)