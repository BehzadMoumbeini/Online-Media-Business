# Generated by Django 3.2 on 2022-12-28 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.BooleanField(help_text='femal is False, male is True, null is unset', null=True, verbose_name='gender'),
        ),
    ]