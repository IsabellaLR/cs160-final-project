from django.urls import path

from . import views

urlpatterns = [
    path('screen1/', views.forecast, name='screen1'),
    path('screen2/', views.forecast_alert, name='screen2'),
    path('screen3/', views.comparison, name='screen3'),
    path('screen4/', views.comparison_alert, name='screen4'),
    path('', views.index, name='index'),
]