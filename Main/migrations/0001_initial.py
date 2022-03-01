# Generated by Django 3.2.3 on 2022-02-07 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OurWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('subtitle', models.CharField(max_length=200)),
                ('buttonName', models.CharField(max_length=200)),
                ('buttonLink', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('headerImage', models.ImageField(upload_to='')),
                ('sliderImages1', models.ImageField(upload_to='')),
                ('sliderImages2', models.ImageField(blank=True, null=True, upload_to='')),
                ('sliderImages3', models.ImageField(blank=True, null=True, upload_to='')),
                ('sliderImages4', models.ImageField(blank=True, null=True, upload_to='')),
                ('sliderVideo', models.FileField(blank=True, null=True, upload_to='')),
                ('workDescription', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subtitle', models.CharField(max_length=200)),
                ('ourWork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.ourwork')),
                ('tags', models.ManyToManyField(related_name='tags', to='Main.Tag')),
            ],
        ),
    ]
