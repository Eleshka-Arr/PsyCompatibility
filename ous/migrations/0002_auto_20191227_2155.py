# Generated by Django 3.0.1 on 2019-12-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ous', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ous',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]