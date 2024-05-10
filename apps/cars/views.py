from apps.cars.models import CarsModel
from apps.cars.serializers import CarSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .filters import car_filter


#
# class View(GenericAPIView):
#     queryset = CarsModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         qs = self.get_queryset()
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(rise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class Crud(GenericAPIView):
#     queryset = CarsModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         car = self.get_object()
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         data = self.request.data
#         car = self.get_object()
#         serializer = self.get_serializer(car, data)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         data = self.request.data
#         car = self.get_object()
#         serializer = self.get_serializer(car, data, partial=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#


class View(ListCreateAPIView):
    # queryset = CarsModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params.dict())


class Crud(RetrieveUpdateDestroyAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarSerializer
    #
    # def get_queryset(self):
    #     return car_filter(self.request.query_params.dict())
