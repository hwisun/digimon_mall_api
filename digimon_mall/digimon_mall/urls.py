"""digimon_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls.user_urls')),
    path('me/', include('user.urls.me_urls')),
    path('monsters/', include('monster.urls.monster_urls')),
    path('attris/', include('monster.urls.attri_urls')),
    path('geners/', include('monster.urls.gener_urls')),
    path('kinds/', include('monster.urls.kind_urls')),
    path('lists/', include('monster.urls.list_urls')),
    path('media/uploads/monster_images/<str:file_name>', views.image_view),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
