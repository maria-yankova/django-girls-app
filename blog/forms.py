from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    # choose model for this form (Post)
    class Meta:
        model = Post
        fields = ('title', 'text',)
