from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ created time / updated time stamping model """

    created = models.DateTimeField(auto_now_add=True)
    # option "auto_now_add" : record just first timeline as created
    updated = models.DateTimeField(auto_now=True)
    # option "auto_now" : record every timeline as modified

    class Meta:
        abstract = True
        # abstract Model setting in python
