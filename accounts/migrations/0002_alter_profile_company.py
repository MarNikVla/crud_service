# Generated by Django 3.2.5 on 2021-07-27 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='companies.company'),
        ),
    ]
