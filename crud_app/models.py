from django.db import models

class CompanyModel(models.Model):
    name = models.CharField(max_length=80)
    sex = models.CharField(max_length=15)
    age = models.IntegerField()



class UserModel(models.Model):
    name = models.CharField(max_length=80)
    sex = models.CharField(max_length=15)
    age = models.IntegerField()
    group = models.ForeignKey(to='CompanyModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name