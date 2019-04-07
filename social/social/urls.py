from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from mysocial import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysocial.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='mysocial/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mysocial/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)