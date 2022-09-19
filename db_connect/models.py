from django.db import models


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    price = models.IntegerField()

    class Meta:
        db_table = 'books'

