
from django.urls import path, include

urlpatterns = [
    # path('cars', View.as_view()),
    # path('cars/<int:pk>', Crud.as_view())
    path('cars', include('apps.cars.urls'))
]
