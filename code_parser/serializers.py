from rest_framework import serializers

from .models import LocodeCode


class LocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocodeCode
        fields = (
            "id",
            "change_indicator",
            "locode_country_code",
            "locode_location_code",
            "name",
            "name_wo_diacritics",
            "sub_division",
            "function",
            "status",
            "date",
            "iata",
            "coordinates",
            "remarks",
        )
