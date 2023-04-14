### blog-app-2

Integrate CKEditor to your Django Admin

1. Install the Django-CKEditor
```
$ pip3 install django-ckeditor
```

2. Add the CKEditor to the installed_apps in settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor', # CKEditor config
    'ckeditor_uploader', # CKEditor media uploader
]
```
3. Adding path for media files in settings.py
```
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#ckeditor upload path
CKEDITOR_UPLOAD_PATH="uploads/"
```
4. Setup URLs: in the project urls.py, we need to add two things. First is the CKEditor URL and the path of the media files where Django can identify the location of media files.
```
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path

]

# Path of media files
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
5. Change in the model : models.py
```
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=255)
    #body = models.TextField() 
    body = RichTextUploadingField() # CKEditor Rich Text Field

    def __str__(self):
        return self.title
```
6. Run all migrations and migrate
```
$ python manage.py makemigrations
$ python manage.py migrate
```

