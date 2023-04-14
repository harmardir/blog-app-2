from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField



class Post(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField()
    intro = models.TextField()
    #body = models.TextField()
    body = RichTextUploadingField() # CKEditor Rich Text Field
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post , related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(default="user@email.com")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ('-created_at',)

