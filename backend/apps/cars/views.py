from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import CarFilter
from .models import CarModel
from .serializers import CarPhotoSerializer, CarSerializer


class CarListCreateView(ListAPIView):
    """List of all Cars"""

    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    permission_classes = AllowAny,

    def get_queryset(self):
        query = self.request.query_params.dict()
        # CarModel.my_func.lt_seats()
        queryset = super().get_queryset()

        if (year := query.get('lt_grad_year')) and year.isdigit():
            queryset = queryset.filter(grad_year__lt=year)
        if (auto_park_id := query.get('auto_park_id')) and auto_park_id.isdigit():
            queryset = queryset.filter(auto_park_id=auto_park_id)
        return queryset


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get Car by id
    patch:
        Partial update Car by id
    put:
        Full update Car by id
    delete:
        Delete Car by id
    """

    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class AddPhotoToCar(GenericAPIView):
    """
    Post Photo by Car id
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def post(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for key in files:
            serializer = CarPhotoSerializer(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        car_serializer = CarSerializer(car)
        return Response(car_serializer.data, status.HTTP_201_CREATED)
