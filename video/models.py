from django.db import models
from django.db.models import Model, CharField,PositiveIntegerField,TextField,URLField, DateTimeField

# Create your models here.
class Video(Model):
    title = CharField(max_length=150, unique=True)
    #by default all false
    views=PositiveIntegerField(default=1)
    description = TextField(max_length=1000)
    link = URLField(max_length=500)
    published_date = DateTimeField(auto_now_add=True)
    tags=CharField(max_length=300,default="creator,stuff")
    #for new fields always create
    #make migrations when you make new model or column
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published_date']
        #ordering = ['-published_date'] will reverse the order