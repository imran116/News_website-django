# Generated by Django 4.2.1 on 2023-09-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_websitesetting_copy_right'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_us/')),
                ('paragraph_one', models.TextField()),
                ('paragraph_two', models.TextField()),
                ('paragraph_three', models.TextField()),
                ('paragraph_four', models.TextField()),
            ],
        ),
    ]
