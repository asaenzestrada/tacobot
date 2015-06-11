from django.shortcuts import render_to_response
from django.template.context import RequestContext


# Create your views here.
def system(request):
    if request.POST:
        return True
    else:
        obj =  dict()
        obj['as'] = 'asdasd'
        obj['asfasd'] = 1
        return render_to_response('index.html', obj, context_instance=RequestContext(request))