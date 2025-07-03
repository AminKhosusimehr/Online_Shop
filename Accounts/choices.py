from django.db import models


class gender_choices(models.TextChoices):
    MALE = 'Male' , 'Male'
    FEMALE = 'Female' , 'Female'
    OTHER = 'Other' , 'Other'