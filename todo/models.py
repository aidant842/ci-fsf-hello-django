from django.db import models

# Create your models here.


class Item(models.Model):
    """ null and blank being set to false stops items being
    created without a name programatically,
    and will make the field required on forms
    whether done by python code,
    a user in a web form or even in the admin panel
    default being False always assigns False by default """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
