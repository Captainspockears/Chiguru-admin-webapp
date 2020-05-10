# Generated by Django 3.0.5 on 2020-05-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileadmin', '0003_auto_20200509_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
                ('image', models.ImageField(upload_to='mobileadmin/static/mobileadmin/images/cache')),
            ],
        ),
    ]
