from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class FoodInfo(models.Model):
    info_title = models.CharField(max_length=100, null=True)
    info_content = models.TextField(max_length=10000, null=True)
    info_image = models.ImageField(null=True, blank=True, upload_to="book-image")

    def __str__(self):
        return self.info_title


class Comment(models.Model):
    info_post = models.ForeignKey('foodInfo.FoodInfo', on_delete=models.CASCADE, blank=True, null=True)
    info_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    info_comment = models.CharField(max_length=150, null=True)
    info_time = models.DateTimeField(auto_now_add=True, null=True, primary_key=False)
