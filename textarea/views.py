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
from django.conf import settings
import json

def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == 'POST':
        form = TextAreaForm(request.POST)
#	raw = request.POST['describe'].split("\"") #print form
#	data = raw[1]
#	data  = data.split(",")[1]
#	print data
#	url = "/home/hadoolytics-deepak/workspace/tinymce/quiz/quiz/media/photos/item.jpg" #str(settings.MEDIA_URL)+"photos/item.jpg"
#	print url
#	file = open(url,"wb")
#	file.write(data.decode('base64'))
#	raw[1] = url
#	print "--------------", raw
#	final = ""
#	for item in raw:
#	    final = final+item
#	post = request.POST.copy()
#	post['describe']=final
#	print post
#	print '----fawbve-----'
        if form.is_valid():
	    print "valid hai"
	    form.save() #post
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
    print "ondropeddddd --------------------------------"
    #print request
    data = request.GET.keys()[0].split(',')[1] + "=="
    data = data.replace(" ", "+")
    print data
    #data2 = request.GET.values()[1]
    #data = data2 + ";" + data1
    
    url = "/home/hadoolytics-deepak/workspace/tinymce/quiz/quiz/media/photos/item1.png" 
    file = open(url,"wb")
    print 1
    file.write(data.decode('base64'))
    file.close()
    print 2
    final = {"location": "media/photos/item1.png"}
    print 3
    js_data = json.dumps(final)
    print js_data
    return HttpResponse(js_data)
