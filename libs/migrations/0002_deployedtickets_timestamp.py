# Generated by Django 3.2.5 on 2021-07-17 21:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployedtickets',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
