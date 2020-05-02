from django.urls import path
from visualisation import views


app_name = 'visuals'


urlpatterns = [
    path('visuals/home/', views.VisualHome.as_view(), name='visuals-home'),
    path('visuals/first/', views.FirstVisual.as_view(), name='first-visual'),
    path('visuals/basic-static-chart/', views.BasicStaticChartVisual.as_view(), name='basic-static-chart'),
    path('visuals/basic-shapes/', views.BasicShapesVisual.as_view(), name='basic-shapes'),
]