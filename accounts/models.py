from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.urls import reverse_lazy

from companies.models import Company

def get_stab_company_id():
    return Company.objects.get(title__exact='No company').id

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
                                on_delete=models.SET(get_stab_company_id))
    is_admin = models.BooleanField('Администратор', default=False)
    is_moderator = models.BooleanField('Модератор', default=False)

    def __str__(self):
        return '{}'.format(self.user.username)

    def get_absolute_url(self):
        return reverse_lazy('accounts:user_detail', kwargs={'pk': self.pk})

@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    """Creating stub company"""
    if created:
        try:
            Company.objects.get(title__exact='No company')
        except ObjectDoesNotExist:
            Company.create_stub_company().save()

        # Creating Profile if create User
        Profile.objects.create(user=instance, company=Company.objects.get(title__exact='No company'))
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

# Delete User if delete Profile
@receiver(post_delete, sender=Profile)
def del_user(sender, instance, **kwargs):
    User.objects.get(id__exact=instance.user.id).delete()

