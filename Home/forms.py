from django import forms
from froala_editor.widgets import FroalaEditor
from .models import Blog

class FroalaBlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ['content']