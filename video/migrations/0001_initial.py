# Generated by Django 3.1.2 on 2021-08-16 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('views', models.PositiveIntegerField(default=1)),
                ('description', models.TextField(max_length=1000)),
                ('link', models.URLField(max_length=500)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['published_date'],
            },
        ),
    ]
