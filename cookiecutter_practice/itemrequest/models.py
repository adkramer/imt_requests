from django.db import models
from django.shortcuts import render, reverse
from django_extensions.db.models import TimeStampedModel

from django.forms.models import model_to_dict

class Uom(models.Model):
    name = models.CharField("Unit of Measure", max_length=30)
    abbreviation = models.CharField("Abbreviated UOM", max_length=10)

    def __str__(self):
        return(str(self.name))

class Manufacturer(models.Model):
    """
    Manufacturer for New Item Request
    """
    name = models.CharField("Manufacturer Name", max_length=60, help_text="Enter Manufacturer's Name")
    part_number = models.CharField("Part Number", max_length=60, help_text="Enter Part Number")

    def __str__(self):
        rtn = self.name + " " + self.part_number
        return str(rtn)

class Vendor(models.Model):
    """
    Vendor for New Item Request
    """
    name = models.CharField("Vendor Name", max_length=60, help_text="Enter Vendors's Name")
    part_number = models.CharField("Part Number", max_length=60, help_text="Enter Part Number")

    def __str__(self):
        rtn = self.name + " " + self.part_number
        return str(rtn)

class ItemRequest(TimeStampedModel):
    """
    Item Request for New Item Request
    """
    SAVED = "1"
    REQUESTED = "2"
    DENIED = "3"
    APPROVED = "4"
    item_name = models.CharField("Item Name", max_length=255)
    description = models.TextField(help_text="Full description of the item")
    #manufacturer = models.ForeignKey(Manufacturer)
    #vendor = models.ForeignKey(Vendor)
    manufacturer_name = models.CharField("Manufacturer", max_length=255, blank=True)
    manufacturer_number = models.CharField("Manufacturer Part Number", max_length=255, blank=True)
    vendor_name = models.CharField(max_length=255, blank=True)
    vendor_number = models.CharField(max_length=255, blank=True)
    weblink = models.URLField("Web Address", max_length=600, help_text="Enter Link to detail page for the item", blank=True)
    unit = models.ForeignKey(Uom)
    state = models.CharField(max_length=1, choices=[(SAVED, "saved"), (REQUESTED, "requested"), (DENIED, "denied"), (APPROVED, "approved")], default=SAVED,)
    created_by = models.ForeignKey('users.User')
    requester = models.CharField(max_length=60, blank=True, help_text="Name of the person requesting the item")

    def get_absolute_url(self):
        return reverse('requests')

    def submit(self):
        self.state = 2
        self.save()

    def deny(self):
        self.state = 3
        self.save()

    def approve(self):
        self.state = 4
        self.save()

    def __str__(self):
        rtn = " ".join([str(self.id), self.item_name])
        return str(rtn)
    
    def get_fields(self):
        return [(field.get_field_value(self), field._get_val_from_obj(self)) for field in self.__class__._meta.fields]
    
    def get_field_dict(self):
        return reversed(sorted(model_to_dict(self).items()))
    

    