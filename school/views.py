from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

import school
from school.models import Dept,Course


# Create your views here.
def home(request):
    return render(request,"home.html")
def department_list(request):
    course_list = Dept.objects.all()
    return render(request, "home.html", {'context':course_list})