from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    grad_year__gt = filters.NumberFilter(field_name='grad_year', lookup_expr='gt')
    grad_year__lt = filters.NumberFilter(field_name='grad_year', lookup_expr='lt')
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')
    brand_end = filters.CharFilter(field_name='brand', lookup_expr='iendswith')
    brand_contain = filters.CharFilter(field_name='brand', lookup_expr='icontains')

    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = CarModel
        fields = (
            'grad_year__gt', 'grad_year__lt', 'brand_start', 'brand_end', 'brand_contain',
            'price_gt', 'price_lt', 'price_gte', 'price_lte'
        )
