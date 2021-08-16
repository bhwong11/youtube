# Generated by Django 3.1.2 on 2021-08-16 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '0002_video_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='video.video')),
            ],
        ),
    ]