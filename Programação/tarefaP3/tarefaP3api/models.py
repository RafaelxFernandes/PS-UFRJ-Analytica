from django.db import models

class PersonAge(models.Model):

    name = models.CharField(max_length = 60)
    birthdate = models.CharField(max_length = 60)
    random_date = models.CharField(max_length = 60)