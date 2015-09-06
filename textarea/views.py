from django.shortcuts import render
from django.http import HttpResponse
from textarea.models import TextAreaModel
from textarea.forms import TextAreaForm, NameForm
from quiz import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
import json
from django.forms import ModelForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == 'POST':
        form = TextAreaForm(request.POST)
	print form
	print '---------'
        if form.is_valid():
	    print "valid hai"
	    form.save()
    else:
        form = TextAreaForm()
    return render_to_response('name.html', {'form': form}, context_instance=RequestContext(request))

def index1(request):
    return render_to_response('equation_editor.html')


def upload(request):
    print "Upload"
    print request.POST
    print "-------------------"
    print request.FILES
    
    print "++++++++++++++++"
    form = NameForm(request.POST, request.FILES)
    print form
    if form.is_valid():
      print "VVVValid Hai"
      #image = form.save()
      image = request.FILES['image']
      print type(image), "1111"
#      print image.__dict__, image.file, image.fileno, "2211"
      path = default_storage.save('photos/images.jpg', ContentFile(image.read()))
      image_path = "media/" + path
      print path, image_path, ")))))"
      print settings.MEDIA_ROOT
#      tmp_file = os.path.join(settings.MEDIA_ROOT, path)
#      print tmp_file, "--------"
#      print tmp_file.url()
#      print image.get_absolute_url()
      return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('%s');</script>" % image_path) #.val('%s').closest('.mce-window').find('.mce-primary').click()
    print "Final Return"
    return HttpResponse("<script>alert('%s');</script>" % escapejs('\n'.join([v[0] for k, v in form.errors.items()])))

def ondrop(request):
    print "ondropeddddd"
    return HttpResponse("<script>alert('123');</script>")
