# Generated by Django 3.2.5 on 2021-08-01 10:16

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_company_news'),
        ('accounts', '0006_alter_profile_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(on_delete=models.SET(accounts.models.get_stab_company_id), related_name='employee', to='companies.company'),
        ),
    ]
