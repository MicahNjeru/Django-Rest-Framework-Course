from django.urls import path
from django.contrib import admin
from rest_framework import routers

# Rest Framework Router 
router = routers.DefaultRouter()

urlpatterns = router.urls

# Django Default URLs
urlpatterns += [
    path('admin/', admin.site.urls),
]