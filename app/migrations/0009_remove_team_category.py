# Generated by Django 4.1.2 on 2022-12-11 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_hero_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='category',
        ),
    ]