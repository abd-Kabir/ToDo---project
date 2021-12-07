from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('auth_app.urls')),
    path('api/file/', include('file_app.urls')),
    path('api/todo/', include('todo_app.urls')),
    path('admin/', admin.site.urls),
]
