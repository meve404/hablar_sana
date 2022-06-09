from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('@ej8h/', admin.site.urls),
    path('', include('home_app.urls')),
    path('blog-hablar-sana/', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
]
