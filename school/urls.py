from . import views
from django.urls import path
app_name='school'
urlpatterns = [

    path('',views.home,name='home'),
    path('department_list/',views.department_list,name='department_list'),

]
