from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    grad_year__gt = filters.NumberFilter(field_name='grad_year', lookup_expr='gt')
    grad_year__lt = filters.NumberFilter(field_name='grad_year', lookup_expr='lt')
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')

    class Meta:
        model = CarModel
        fields = ('grad_year__gt', 'grad_year__lt', 'brand_start')
