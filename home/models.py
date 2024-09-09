from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class OvozModel(models.Model):
    saylovchi = models.CharField(max_length=100, editable=False)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  

    def save(self, *args, **kwargs):
        
        if not self.saylovchi:
            if self.user:
                self.saylovchi = self.user.get_full_name()
            else:
                
                raise ValueError("User maydonini to'ldirish kerak.")
        super(OvozModel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.saylovchi} - {self.user.username}'