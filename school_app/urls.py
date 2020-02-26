from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homeView, name="Welcome-Home"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)