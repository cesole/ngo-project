from django.shortcuts import render
from children.models import Child

# Create your views here.
def do_search(request):
    children = Child.objects.filter(name__icontains=request.GET['q'])
    return render(request, "children.html", {"children": children})