from django import forms
from foodReceipes.models import *


class CommentIt(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'learn_comment', }
