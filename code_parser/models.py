import uuid

from django.db import models


class LocodeCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    change_indicator = models.CharField(max_length=100, blank=True, null=True)
    locode_country_code = models.CharField(max_length=100, blank=True, null=True)
    locode_location_code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_wo_diacritics = models.CharField(max_length=100, blank=True, null=True)
    sub_division = models.CharField(max_length=100, blank=True, null=True)
    function = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    iata = models.CharField(max_length=100, blank=True, null=True)
    coordinates = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
