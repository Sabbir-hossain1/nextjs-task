from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
     # account app urls
    path('user/', include('account.urls')),
]
