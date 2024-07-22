from django import forms

from blog.models import BlogComment


class BlogCommentsForm(forms.ModelForm):
    parent = forms.CharField(widget=forms.HiddenInput(attrs={'name': 'parent', 'id': 'parent'}), required=False)

    class Meta:
        model = BlogComment
        fields = ['comment']

