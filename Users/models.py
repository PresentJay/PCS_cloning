from django.db import models

# from pracs import models as prac_models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    """ Users model definition """

    birthday = models.DateTimeField(null=True)

    def __str__(self):
        return self.username

    def totalScore(self):
        # videos = prac_models.object.get(user=self.pk)
        videos = models.Prac.objects.filter(user=self.username)
        score = 0
        for vid in videos:
            score += vid.score
        return score
