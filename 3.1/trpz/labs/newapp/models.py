from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)


class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    number = models.CharField(max_length=255, null=True)
