# Generated by Django 4.0.4 on 2022-05-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_userlogin_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userregister',
            name='confirm_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userregister',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
