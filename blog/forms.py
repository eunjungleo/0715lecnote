from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # model은 Post
        fields = ['title', 'author', 'body', 'img'] #사용자에게 입력받을 fields

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'body']