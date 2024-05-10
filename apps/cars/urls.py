from apps.cars.views import View, Crud
from django.urls import path

urlpatterns = [
    path('', View.as_view(), name='cars_list_create'),
    path('/<int:pk>', Crud.as_view(), name='cars_crud')
]
