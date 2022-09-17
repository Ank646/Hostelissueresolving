from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('checklogin',views.checklogin,name="login"),
    path('check',views.check,name="check"),
    path('signup',views.signup,name="signup"),
    path('<str:name>/profile',views.profile,name="profile"),
    path('<str:name>/issues',views.issue,name="issue"),
    path('<str:name>/uissues',views.uissue,name="issue"),
    path('warden',views.warden,name="warden"),
    path('wardencomplains',views.wardencomplains,name="wardencomplaints"),
    path('recentissue',views.recentissue,name="recentissue"),
    
    
    

]
   