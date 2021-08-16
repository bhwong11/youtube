from django.urls import path
from . import views

urlpatterns = [
	# put urls here
	path("<int:video_pk>/comments/new",views.CommentCreate.as_view(),name='comment_create')
]