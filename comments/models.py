from django.db import models
from django.db.models import Model, ForeignKey,CharField
from django.db.models.deletion import CASCADE
from video.models import Video

# Create your models here.
#related name -> video.comments.all
class Comment(Model):
    video = ForeignKey(Video,on_delete=CASCADE,related_name="comments")
    content = CharField(max_length=200)

    def __str__(self):
        return f"{self.pk} - {self.video.title}"