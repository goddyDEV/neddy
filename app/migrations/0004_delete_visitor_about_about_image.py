# Generated by Django 4.1.2 on 2022-12-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_order_received_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Visitor',
        ),
        migrations.AddField(
            model_name='about',
            name='about_image',
            field=models.ImageField(blank=True, null=True, upload_to='about/%Y-%m-%d'),
        ),
    ]
