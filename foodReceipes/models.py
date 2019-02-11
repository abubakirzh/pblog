from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class FoodReceipts(models.Model):
    learn_title = models.CharField(max_length=100, null=True)
    learn_pre_content = models.CharField(max_length=500, null=True)
    learn_content = models.TextField(max_length=10000, null=True)
    learn_image = models.ImageField(null=True, blank=True, upload_to="book-image")

    def __str__(self):
        return self.learn_title


class Comment(models.Model):
    learn_post = models.ForeignKey('foodReceipes.FoodReceipts', on_delete=models.CASCADE, blank=True, null=True)
    learn_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    learn_comment = models.TextField(max_length=150, null=True)
    learn_time = models.DateTimeField(auto_now_add=True, null=True, primary_key=False)