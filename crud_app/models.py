from django.db import models

class CompanyModel(models.Model):
    name = models.CharField(max_length=80)
    sex = models.CharField(max_length=15)
    age = models.IntegerField()



class UserModel(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=80)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(max_length=3)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.name