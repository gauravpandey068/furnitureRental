from django.db import models


# user personal information for renting
class UserInformation(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=10, blank=False, null=False)
    delivery_address = models.CharField(
        max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name
