# Generated by Django 4.2.1 on 2023-05-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_flashnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='slider/')),
            ],
        ),
    ]