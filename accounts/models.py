from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from companies.models import Company

class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField('Фамилия', max_length=50, blank=True)
    first_name = models.CharField('Имя', max_length=50, blank=True)
    middle_name = models.CharField('Отчество', max_length=50, blank=True)
    bio = models.TextField('Информация о себе', max_length=500, blank=True)
    birth_date = models.DateField('Дата рождения: dd/mm.YYYY', null=True, blank=True)
    avatar = models.ImageField('Аватар', upload_to='users/%Y/%m/%d/', blank=True)
    company = models.ForeignKey(Company,
                                related_name='employee',
                                on_delete=models.CASCADE,
                                blank=True)


    # def save(self, *args, **kwargs):
    #     if self.company is None:  # Set default reference
    #         self.company_id = 1
    #     super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.user.username)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def create_company(sender, instance, created, **kwargs):
    """Creating profile if create user"""
    if created:
        # Company.create()
        print('sdf')
        # comp = Company.objects.get(pk=1)
        # print(comp)


# @receiver(post_save, sender=User)
# def save_or_create_profile(sender, instance, created, **kwargs):
#     """Creating profile if create user"""
#     if created:
#         Profile.objects.create(user=instance, company_id=1)
#     else:
#         try:
#             instance.profile.save()
#         except ObjectDoesNotExist:
#             Profile.objects.create(user=instance)
