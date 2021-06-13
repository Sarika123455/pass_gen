from django.contrib import admin
from django.urls import path
from admin_app import views


urlpatterns = [
  
   path('',views.home,name='home'),
   path('signup',views.Signup,name='signup'),
   path('login',views.login,name='login'),
   path('addmember',views.addmember,name='addmember'),
   path('societyloan',views.societyloan,name='societyloan'),
   # path('rdloan',views.rdloan,name='rdloan'),
   # path('loanmember',views.loanmember,name='loanmember'),
   path('allloan/',views.allloan,name='allloan'),
   path('memberread',views.memberread,name='memberread'),
   # path('allloan/<slug:data>',views.allloan,name="allloandata"),
 
   # path('add/',views.add,name='add'),
   path('search',views.search,name='search'),
   path('societyloanread',views.societyloanread,name='societyloanread'),
   path('memberloan',views.memberloan,name='memberloan'),
   path('memberloanform',views.memberloanform,name='memberloanform'),
   path('memberloanread',views.memberloanread,name='memberloanread'),
   path('update/<int:id>',views.loanupdate,name='update'),
   path('delete/<int:id>',views.loandelete,name='delete'),
   path('memberupdate/<int:id>',views.memberupdate,name='memberupdate'),
   path('memberdelete/<int:id>',views.memberdelete,name='memberdelete'),
   path('societyupdate/<int:id>',views.societyupdate,name='societyupdate'),
   path('societydelete/<int:id>',views.societydelete,name='societydelete'),
   path('loansocietyread',views.loansocietyread,name='loansocietyread'),
   path('societysearchloan',views.societysearchloan,name='societysearchloan'),
   # path('monthsearchloan',views.monthsearchloan,name='monthsearchloan'),
   path('userhome',views.userhome,name='userhome'),
   # path('societysearchloans',views.societysearchloans,name='societysearchloans'),



   
   

   
]