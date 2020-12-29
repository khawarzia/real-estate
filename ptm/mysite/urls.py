from django.conf.urls import url
from django.urls import path , include
from . import views
#REST API URLS


from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
 
    url(r'^$', views.home, name="home"),

    # TODO  :   USER LOGIN
    url(r'login/', views.login_user, name = 'login'),

    
    url(r'^logout/$', views.logout_user, name= "logout"),

    # TODO  :   USER REGISTRATION
    url(r'^register/$', views.register_user, name= "register"),


    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    url(r'edit-profile/$', views.edit_profile, name="editProfile"),
    url(r'edit-profile-inform/$', views.edit_profile_user, name="editProfileUSer"),

    #Password Change URL............
    url(r'^change_password/$', views.change_password, name = "change_password"),

    # ! PROFILE URL
    url('my_profile',views.myprofile, name='pro'),

    #TODO   :   PASSWORD RESET URLS ...
    path('password_reset/', PasswordResetView.as_view(), name='password_reset' ),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('contact/', views.contact, name= "contact"),

    path('form1', views.form1, name='form1'),
    path('form2', views.form2, name='form2'),
    path('form3', views.form3, name='form3'),

    path('form11', views.form11, name='form11'),
    path('form21', views.form21, name='form21'),
    path('form31', views.form31, name='form31'),


    path('changeselopt/<int:a>', views.changeopt, name='changeopt'),

    path('get-all-data/<int:sel>/<str:val>', views.newfunc),
    path('get-all-data-buyer/<int:sel>/<str:val>/<str:usr>', views.newfunc2),

]