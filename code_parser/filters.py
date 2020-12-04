from django_filters import rest_framework as filters

from .models import LocodeCode


class LocodeFilter(filters.FilterSet):
    code = filters.CharFilter(field_name="function", lookup_expr="icontains")
    name_wo_diacr = filters.CharFilter(
        field_name="name_wo_diacritics", lookup_expr="icontains"
    )

    class Meta:
        model = LocodeCode
        fields = ("code", "name_wo_diacr")
