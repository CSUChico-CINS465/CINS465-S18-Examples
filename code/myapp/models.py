from django.db import models

from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Suggestion_Model(models.Model):
    suggestion = models.CharField(max_length=240)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(
                        User,
                        on_delete=models.CASCADE
                )

    def __str__(self):
        return "Suggestion " + str(self.id) + ": " + str(self.suggestion)

class Comment_Model(models.Model):
    comment=models.CharField(max_length=240)
    author = models.ForeignKey(
                        User,
                        on_delete=models.CASCADE
                )
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    suggestion = models.ForeignKey(
                        Suggestion_Model,
                        on_delete=models.CASCADE
                )

    def __str__(self):
        return self.comment + " " + str(self.created_on)
