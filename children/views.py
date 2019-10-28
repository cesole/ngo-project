from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Child

# Create your views here.


def all_children(request):
    children = Child.objects.all()
    paginator = Paginator(children, 6)
    
    page = request.GET.get("page")
    
    try:
        children = paginator.page(page)
    except PageNotAnInteger:
        children = paginator.page(1)
    except EmptyPage:
        children = paginator.page(paginator.num_pages)
        
        
    return render(request, "children.html", {"children": children})
    
    
    
    
