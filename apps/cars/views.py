from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    # permission_classes = (AllowAny,)

    def get_queryset(self):
        query = self.request.query_params.dict()

        queryset = super().get_queryset()

        if (year := query.get('lt_grad_year')) and year.isdigit():
            queryset = queryset.filter(grad_year__lt=year)
        if (auto_park_id := query.get('auto_park_id')) and auto_park_id.isdigit():
            queryset = queryset.filter(auto_park_id=auto_park_id)
        return queryset

    # def get(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def get(self, *args, **kwargs):
    # qs = CarModel.objects.all()
    # query = self.request.query_params.dict()
    # year = query.get('lt_year')
    # if year:
    #     qs = qs.filter(grad_year__gt=year)
    # qs = qs.filter(brand__icontains='gt').filter(grad_year__range=(2013, 2020))
    # qs = qs.order_by('brand')
    # qs = qs.exclude(brand='X88')
    # print(qs.count())
    # serializer = CarSerializer(self.get_queryset(), many=True)
    # return Response(serializer.data, status.HTTP_200_OK)

    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = CarSerializer(data=data)
    #
    #     # if not serializer.is_valid():
    #     #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    #
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    # def get(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def get(self, *args, **kwargs):
    #     # pk = kwargs.get('pk')
    #     # qs = CarModel.objects.all()
    #     # exists = CarModel.objects.filter(pk=pk).exists()
    #     #
    #     # if not exists:
    #     #     return Response("Not Found", status.HTTP_404_NOT_FOUND)
    #     #
    #     # car = CarModel.objects.get(pk=pk)
    #     # car = get_object_or_404(qs, pk=pk)
    #     car = self.get_object()
    #     serializer = CarSerializer(car)
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def put(self, *args, **kwargs):
    #     # pk = kwargs.get('pk')
    #     data = self.request.data
    #     # exists = CarModel.objects.filter(pk=pk).exists()
    #
    #     # if not exists:
    #     #     return Response("Not Found", status.HTTP_404_NOT_FOUND)
    #     #
    #     # car = CarModel.objects.get(pk=pk)
    #     car = self.get_object()
    #     serializer = CarSerializer(car, data)
    #     serializer.is_valid(raise_exception=True)
    #     # if not serializer.is_valid():
    #     #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    #
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def patch(self, *args, **kwargs):
    #     # pk = kwargs.get('pk')
    #     data = self.request.data
    #     # exists = CarModel.objects.filter(pk=pk).exists()
    #
    #     # if not exists:
    #     #     return Response("Not Found", status.HTTP_404_NOT_FOUND)
    #
    #     # car = CarModel.objects.get(pk=pk)
    #     car = self.get_object()
    #     serializer = CarSerializer(car, data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     # if not serializer.is_valid():
    #     #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    #
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def delete(self, *args, **kwargs):
    #     # pk = kwargs.get('pk')
    #     # exists = CarModel.objects.filter(pk=pk).exists()
    #     #
    #     # if not exists:
    #     #     return Response("Not Found", status.HTTP_404_NOT_FOUND)
    #     #
    #     # car = CarModel.objects.get(pk=pk)
    #     # car.delete()
    #     self.get_object().delete()
    #     return Response('The car was deleted', status.HTTP_204_NO_CONTENT)
