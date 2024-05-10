from rest_framework import serializers
from apps.cars.models import CarsModel


# class CarSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     brand = serializers.CharField(max_length=50)
#     year = serializers.IntegerField()
#     v = serializers.FloatField()
#     body = serializers.CharField(max_length=30)
#     price = serializers.IntegerField()

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('id', 'brand', 'year', 'v', 'body', 'price', 'created_at', 'updated_at')

    def create(self, validated_data):
        car = CarsModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


