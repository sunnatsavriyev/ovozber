from django.db import models
from django.contrib.auth.models import User

class OvozModel(models.Model):
    user = models.ForeignKey(User, related_name='votes_received', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'
