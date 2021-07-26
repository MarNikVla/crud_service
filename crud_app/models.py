from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class CompanyModel(models.Model):
    title = models.CharField(max_length=80)
    active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    foundation_date = models.DateField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})