# Generated by Django 3.2.3 on 2021-06-13 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
