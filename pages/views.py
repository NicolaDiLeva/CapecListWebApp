from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

#import delle classi
from data.models import *

def home_view(request):
    
    return render(request, "pages/home.html")


#def query_meta_view(request):
#   
#   #query meta
#   obj = DomainsOfAttack.objects.filter(abstraction="Meta")
#   
#   filter = DataFilter(request.GET, queryset=obj)
#    obj = filter.qs
#    
#    context = {
#        'object': obj,
#        'filter': filter
#    }
#    return render(request, "pages/query.html", context)

#query id(fisso)
def id_view(request):

    obj = DomainsOfAttack.objects.filter(id=151)
    context = {
       'object': obj
    }
    return render(request, "pages/query.html", context)
    
    
#query ParentOf
def parent_view(request):

   obj = DomainsOfAttack.objects.filter(relatedattackpatterns__icontains="151")
   context = {
       'object': obj
  }
   
   return render(request, "pages/query.html", context)
    
#query meta
def meta_view(request):

    obj = DomainsOfAttack.objects.filter(abstraction="Meta")
    context = {
        'object': obj
    }
    
    return render(request, "pages/query.html", context)

#prova id
#def id_view(request):
#   
#   qs = DomainsOfAttack.objects.all()
#    
#    id_query = request.GET.get('id')
#    print(id_query)
#    
#    context = {
#        'queryset': qs
#    }
#    return render(request, "pages/id.html", context)