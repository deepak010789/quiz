from django.shortcuts import render
from django.http import HttpResponse
from textarea.models import TextAreaModel
from textarea.forms import TextAreaForm

from django.template import RequestContext
from django.shortcuts import render_to_response
import json

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
    form = myForm(request.POST, request.FILES)
    print form
    if form.is_valid():
      print "VVVValid Hai"
      image = form.save()
      return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('%s').closest('.mce-window').find('.mce-primary').click();</script>" % image.get_absolute_url())
    print "Final Return"
    return HttpResponse("<script>alert('%s');</script>" % escapejs('\n'.join([v[0] for k, v in form.errors.items()])))
