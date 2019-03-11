from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('createUser/',views.createUser,name='createUser'),
    path('allRecipies/',views.allRecipies,name='allRecipies'),
    path('newRecipies/',views.newRecipies,name='newRecipies'),
    path('profilePage/',views.profilePage,name='profilePage'),
    path('editProfile/<int:ID>/',views.editProfile,name='editProfile'),
    path('details/',views.details,name='details'),

]