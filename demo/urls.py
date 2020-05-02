from django.urls import path
from demo import views


app_name = 'demo'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('user/list/', views.UserList.as_view(), name='userlist'),
    path('user/create/', views.UserCreate.as_view(), name='usercreate'),
    path('employee/list/', views.EmployeeList.as_view(), name='emplist'),
    path('employee/create/', views.EmployeeCreate.as_view(), name='empcreate'),
    path('technology/list/', views.TechnologyList.as_view(), name='techlist'),
    path('project/list/', views.ProjectList.as_view(), name='projectlist'),
    path('project2/list/', views.Project2List.as_view(), name='project2list'),
    path('project2team/list/', views.Project2TeamList.as_view(), name='project2teamlist'),
]