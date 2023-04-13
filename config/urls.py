from django.contrib import admin
from django.urls import path , include , re_path
from django.conf.urls.static import static
from django.conf import settings
from core.views import frontpage , about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', include('blog.urls')),
    path('', frontpage, name='frontpage'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path
   
]

# Path of media files
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
