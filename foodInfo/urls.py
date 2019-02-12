from django.urls import path
from foodInfo.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', show_info, name="show_info"),

]
