from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category , name = 'posts', on_delete=models.CASCADE)
    title = models.CharField(max_length= 255)
    slug = models.SlugField()
    intro = models.TextField()
    #body = models.TextField()
    body = RichTextUploadingField() # CKEditor Rich Text Field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post , related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(default="user@email.com")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

