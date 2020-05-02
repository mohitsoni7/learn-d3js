from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User

from demo.models import *
from demo.forms import *


class Home(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UserList(ListView):
    model = User
    template_name = 'userlist.html'
    context_object_name = 'users'



class UserCreate(CreateView):
    model = User
    template_name = 'usercreate.html'
    form_class = UserCreateForm
    
    def get_success_url(self):
        return reverse('demo:userlist')
    


class EmployeeList(ListView):
    model = Employee
    template_name = 'employeelist.html'
    context_object_name = 'employees'


class EmployeeCreate(CreateView):
    model = User
    template_name = 'employeecreate.html'
    form_class = EmployeeCreateForm

    def get_success_url(self):
        return reverse('demo:emplist')


class ProjectList(ListView):
    model = Project
    template_name = 'projectlist.html'


class TechnologyList(ListView):
    model = Technology
    template_name = 'technologylist.html'


class Project2List(ListView):
    model = Project2
    template_name = 'project2list.html'


class Project2TeamList(ListView):
    model = Project2Team
    template_name = 'project2teamlist.html'
