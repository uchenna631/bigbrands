from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """ Comment form"""
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    """
    A form to post adding and editing posts
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'content',
            'featured_image',
            'excerpt',
            'status',
         )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your post title'
                 }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'username',
                'value': '',
                'type': 'hidden'
                }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control padding',
                "rows": 2,
                "cols": 20,
                'placeholder': 'Summary of Post Here'
                })
        }