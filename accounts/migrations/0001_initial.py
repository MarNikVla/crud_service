# Generated by Django 3.2.5 on 2021-07-27 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('bio', models.TextField(blank=True, max_length=500, verbose_name='Информация о себе')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения: dd.mm.YYYY')),
                ('avatar', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/', verbose_name='Аватар')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='companies.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]