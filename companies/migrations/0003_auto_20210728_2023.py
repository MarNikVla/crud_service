# Generated by Django 3.2.5 on 2021-07-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_company_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterField(
            model_name='company',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='company /%Y/%m/%d/', verbose_name='Аватар'),
        ),
    ]
