from django.db import models
from core import models as core_models

# Create your models here.


class Prac(core_models.TimeStampedModel):

    """ Pracs Video models definition """

    title = models.CharField(max_length=100)
    class_vid = models.ForeignKey(
        "classes.Class", related_name="pracs", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        "users.User", related_name="pracs", on_delete=models.CASCADE
    )
    video = models.FileField(upload_to="pracs/", null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title
