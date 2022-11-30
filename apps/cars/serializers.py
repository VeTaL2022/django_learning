from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers

from .models import CarModel


# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     brand = serializers.CharField()
#     grad_year = serializers.IntegerField()
#     n_seats = serializers.IntegerField()
#     body_type = serializers.CharField()
#     engine_cap = serializers.FloatField()
#
#     def update(self, instance: CarModel, validated_data: dict):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         return CarModel.objects.create(**validated_data)

class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        exclude = ('auto_park',)

# class CarSpecificSerializer(ModelSerializer):
#     class Meta:
#         model = CarModel
#         fields = ('id', 'brand', 'grad_year')
