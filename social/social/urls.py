from django.conf import settings
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from mysocial import views as user_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysocial.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='mysocial/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mysocial/logout.html'), name='logout'),
    path('users/', include('friends.urls')),
    path('accounts/', include('allauth.urls')),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    # path('auth/', include('rest_framework.urls',
    #                        namespace='rest_framework')),
]


apipatterns = [
    path('', include('mysocial.urls')),
]

urlpatterns+= [
    path('api/v1/', include(apipatterns)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)