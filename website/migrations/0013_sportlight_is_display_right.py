# Generated by Django 4.2.1 on 2023-05-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_sportlight_delete_spotlight'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportlight',
            name='is_display_right',
            field=models.BooleanField(default=False),
        ),
    ]