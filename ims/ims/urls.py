
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),  
    path('items/', include('items.urls')),  
    path('__debug__/', include('debug_toolbar.urls')),
]       