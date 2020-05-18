from django.db import models
from core import models as core_models

# Create your models here.


class Class(core_models.TimeStampedModel):

    """ Classes Video Model Definition """

    HIGH = "상"
    MIDDLE = "중"
    LOW = "하"

    LEVEL_CHOICES = (
        (HIGH, "상"),
        (MIDDLE, "중"),
        (LOW, "하"),
    )

    title = models.TextField(blank=False)
    video = models.FileField(upload_to="classes/", null=True)
    thumbnail = models.ImageField(upload_to="")
    views_count = models.PositiveIntegerField(default=0)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=5, default=LOW)

    def __str__(self):
        return self.title + ": " + str(self.videofile)
