from django import forms
from foodInfo.models import *


class CommentIt(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'info_comment', }
