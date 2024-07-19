from django.contrib import admin
from django.urls import path, include
from app.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('', home, name='home'),  # This should handle the root URL
]
