from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from textarea.models import TextAreaModel
from django.contrib import admin

class TextAreaForm(forms.ModelForm):
    describe = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
#    class Media:
#        js = ('tiny_mce.js','tiny_mce_src.js',)
    class Meta:
        model = TextAreaModel

#class TextAreaAdmin(admin.ModelAdmin):
#    form = TextAreaForm

#    class Admin:
#        js = ('tiny_mce/tiny_mce.js',
#            'tiny_mce/textareas.js',
#        )
