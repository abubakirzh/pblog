"""pblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

from foodReceipes.views import *
from foodInfo.views import *
from Auth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show, name="show_main"),
    path('info/', include('foodInfo.urls')),
    path('info/<int:post_id>/', info_detail, name='info_detail'),
    path('learn/', show_receipts, name="show_receipts"),
    path('learn/<int:post_id>/', learn_detail, name='learn_detail'),
    path('search', search_food_info, name="search_food_info"),
    path('searches', search_food_learn, name="search_food_learn"),

    url(r'^profile/(?P<pk>\d+)/$', view_profile, name='view_profile_with_pk'),
    path('login/', login_user, name="login_user"),
    path('logout', logout_user, name="logout_user"),
    path('register', register_user, name="register_user"),
    path('edit', edit_user_profile, name="edit_user_profile"),
    path('password', change_password, name="change_password"),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

