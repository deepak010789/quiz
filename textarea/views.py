from django.shortcuts import render
from django.http import HttpResponse
from textarea.models import TextAreaModel
from textarea.forms import TextAreaForm

from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == 'POST':
        form = TextAreaForm(request.POST)
        if form.is_valid():
	    print "hahah"
	    form.save()
    else:
        form = TextAreaForm()
    return render_to_response('name.html', {'form': form}, context_instance=RequestContext(request))
