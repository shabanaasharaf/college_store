from . import views
from django.urls import path

urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('new_page/',views.view,name='view'),
    path('login/personal_info/',views.info,name='info'),
    path('logout/',views.logout,name='logout'),
    path('login/home/',views.home,name='home')

]
