import datetime
from django.db import models
import uuid

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    step_name_one = models.CharField(max_length=100, blank=True, null=True)
    planned_date_one = models.DateTimeField(blank=True, null=True)
    actual_date_one = models.DateTimeField(blank=True, null=True)
    status_one = models.CharField(max_length=20)
    timedelay_one = models.DurationField(null=True, blank=True)
    step_name_two = models.CharField(max_length=100, blank=True, null=True)
    planned_date_two = models.DateTimeField(blank=True, null=True)
    actual_date_two = models.DateTimeField(blank=True, null=True)
    status_two = models.CharField(max_length=20)
    timedelay_two = models.DurationField(null=True, blank=True)
    order_form = models.CharField(max_length=100, blank=True)
    unique_key = models.CharField(max_length=100,default=uuid.uuid4, editable=False, blank=True)

    def __str__(self):
        return (f"{self.company_name}")


class Order_Form(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    step_name_one = models.CharField(max_length=100, blank=True, null=True)
    planned_date_one = models.DateTimeField(blank=True, null=True)
    actual_date_one = models.DateTimeField(blank=True, null=True)
    status_one = models.CharField(max_length=20)
    timedelay_one = models.DurationField(null=True, blank=True)
    step_name_two = models.CharField(max_length=100, blank=True, null=True)
    planned_date_two = models.DateTimeField(blank=True, null=True)
    actual_date_two = models.DateTimeField(blank=True, null=True)
    status_two = models.CharField(max_length=20)
    timedelay_two = models.DurationField(null=True, blank=True)
    unique_key = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return (f"{self.company_name}")