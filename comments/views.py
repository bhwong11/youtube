from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from .models import Comment
from video.models import Video

# Create your views here.
class CommentCreate(View):
    def post(self,request,video_pk):
        content = request.POST.get('content')
        #can use bracket but get returns None whereas brackets reutrns an error
        related_video = Video.objects.get(pk=video_pk)
        Comment.objects.create(content=content,video=related_video)
        return redirect('feed')

