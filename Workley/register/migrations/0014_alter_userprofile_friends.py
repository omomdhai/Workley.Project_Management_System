# Generated by Django 4.2.3 on 2023-07-31 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20230424_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='register.userprofile'),
        ),
    ]
