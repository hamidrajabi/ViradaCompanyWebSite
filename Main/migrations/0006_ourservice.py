# Generated by Django 3.2.3 on 2022-02-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_ourwork_headerimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('text', models.CharField(max_length=2000)),
            ],
        ),
    ]
