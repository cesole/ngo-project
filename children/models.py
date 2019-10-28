from django.db import models

# Create your models here.


class Child(models.Model):
    
    GENDER = (
        ('M','Male'),
        ('F','Female')
    )
    name = models.CharField(max_length=254, default="")
    gender = models.CharField(max_length=6, choices=GENDER)
    birthday =models.DateField()
    enjoys = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name