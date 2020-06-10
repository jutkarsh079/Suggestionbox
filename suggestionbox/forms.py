from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = {'type', 'title', 'text', 'name'}

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'*optional'}),
          #  'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': TinyMCE(attrs={'cols': '30', 'rows':'5'})
        }

