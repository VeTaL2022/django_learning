from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

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
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
