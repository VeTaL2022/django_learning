from django_filters import rest_framework as filters

from .models import AutoParkModel


class AutoParkFilter(filters.FilterSet):
    car_year_lt = filters.NumberFilter(field_name='cars__grad_year', lookup_expr='lt')
    car_year_gt = filters.NumberFilter(field_name='cars__grad_year', lookup_expr='gt')

    class Meta:
        model = AutoParkModel
        fields = 'car_year_lt', 'car_year_gt'
