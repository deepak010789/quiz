from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
#from textarea.models import TextAreaModel

class TextAreaForm(forms.ModelForm):
    describe = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = FlatPage
