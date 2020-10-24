from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # posts endpoints
    path('api/', include('posts.urls')),

]
