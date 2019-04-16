from django.shortcuts import render, get_object_or_404
from models import Craft
from models import Work

def index(request):
    #pull all crafts objects
    Crafts =Craft.objects.all()
    context = {'Craft':Craft,}
    return render(request, 'artist/index.html', {'Craft':Craft})
    
#http 404 error
def detail(request, work_id):
    Work = get_object_or_404(Work, id=work_id)
    return render(request, 'artist/detail.html', {'Work': Work})
