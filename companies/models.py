from django.db import models
from django.urls import reverse


class Company(models.Model):
    """Company model"""
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Информация о компании', max_length=500, blank=True)
    foundation_date = models.DateField('Дата основания: dd/mm/YYYY', null=True, blank=True)
    avatar = models.ImageField('Аватар', upload_to='company/%Y/%m/%d/', blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'pk': self.pk})

    @classmethod
    def create(cls, title='No company'):
        company = cls(title=title).save()
        # do something with the book
        return company

    class Meta:
         verbose_name = "Company"
         verbose_name_plural = "Companies"