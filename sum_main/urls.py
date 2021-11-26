from django.urls import path
from.views import index,services,result_sum
urlpatterns = [
    path('', index, name='index'),
    path('services', services, name='services_1'),
    path('result', result_sum, name='result_1'),
    ]