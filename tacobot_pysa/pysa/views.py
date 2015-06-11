from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def system(request):
    if request.method == 'POST':
        #from util_dev.taco import hazTaco
        for n in range(int(request.POST.get('q', ''))):
            a = n
            hazTaco()
        return render_to_response('index.html', dict(), context_instance=RequestContext(request))
        
    
    return render_to_response('index.html', dict(), context_instance=RequestContext(request))
