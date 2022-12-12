# Generated by Django 4.1.2 on 2022-12-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_testmony_alter_service_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('facebook', 'facebook'), ('twitter', 'twitter'), ('linkedin', 'linkedin'), ('instagram', 'instagram'), ('tiktok', 'tiktok')], max_length=100)),
                ('link', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
