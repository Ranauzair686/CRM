from django.urls import path   #step 12 LINE 1 
from . import views  #step 16 
#STEP 12 LINE 2 
urlpatterns = [
    path('', views.home, name=""),    #step 13 
    path('register',views.register ,name="register"),
    path('my-login',views.my_login ,name="my-login"),
    path('user-logout',views.user_logout ,name="user-logout"),
    path('dashboard',views.dashboard ,name="dashboard"),
    path('create-record',views.create_record ,name="create-record"),
    path('update-record/<int:pk>',views.update_record ,name="update-record"), #stdep 70 
    path('record/<int:pk>',views.singular_record ,name="record"),
    path('delete-record/<int:pk>',views.delete_record ,name="delete-record"), #step 75
]