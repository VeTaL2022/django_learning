from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response

from .models import AutoParkModel
from .serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer
from apps.cars.models import CarModel


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class CarListCreateView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        pk = kwargs.get('pk')
        cars = CarModel.objects.filter(auto_park_id=pk)
        car_serializer = CarSerializer(cars, many=True)
        return Response(car_serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        auto_park_serializer = AutoParkSerializer(auto_park)
        return Response(auto_park_serializer.data)
