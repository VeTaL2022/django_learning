from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import CarModel
from .serializers import CarSerializer, CarSpecificSerializer


class CarListCreateView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        cars = CarModel.objects.all()
        # serializer = CarSerializer(instance=cars, many=True)
        serializer = CarSpecificSerializer(instance=cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response("Not Found", status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = CarModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response("Not Found", status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        serializer = CarSerializer(car, data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = CarModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response("Not Found", status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        serializer = CarSerializer(car, data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    @staticmethod
    def delete(*args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response("Not Found", status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        car.delete()
        return Response('The car was deleted', status.HTTP_204_NO_CONTENT)
