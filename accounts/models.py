from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField('Фамилия', max_length=50, blank=True)
    first_name = models.CharField('Имя', max_length=50, blank=True)
    middle_name = models.CharField('Отчество', max_length=50, blank=True)
    bio = models.TextField('Информация о себе', max_length=500, blank=True)
    birth_date = models.DateField('Дата рождения: dd.mm.YYYY', null=True, blank=True)
    avatar = models.ImageField('Аватар', upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    """Creating profile if create user"""
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
