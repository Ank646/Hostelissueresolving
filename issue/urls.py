from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('checklogin',views.checklogin,name="login"),
    path('check',views.check,name="check"),
    path('signup',views.signup,name="signup"),
    path('<str:name>/issue/add',views.d,name="add"),#whatever is written in invertwd comma in each path it gets added after main page
    path('<str:name>/profile',views.profile,name="profile"),
    path('<str:name>/issues',views.issue,name="issue"),
    path('<str:name>/uissues',views.uissue,name="issues"),
    path('warden',views.warden,name="warden"),
    path('wardencomplains',views.wardencomplains,name="wardencomplaints"),
    path('recentissue',views.recentissue,name="recentissue"),
    
    
    

]
   