from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

#import delle classi
from data.models import *


def home_view(request):
    
    return render(request, "pages/home.html")
    
def query_view(request):
    
    return render(request, "pages/query.html")

def details_view(request, id):
    
    q = DomainsOfAttack.objects.filter(id=id)
    #print(q)
    context = {
        'object': q
    }
    
    return render(request, "pages/details.html", context)
    
#selezione delle views
def DomainsOfAttack_view(request):

    obj = DomainsOfAttack.objects.all()
    context = {
        'object': obj
    }

    return render(request, "pages/list.html", context)

def MechanismsOfAttack_view(request):

    obj = MechanismsOfAttack.objects.all()
    context = {
        'object': obj
    }
    
    return render(request, "pages/list.html", context)

def DeprecatedEntries_view(request):

    obj = DeprecatedEntries.objects.all()
    context = {
        'object': obj
    }
    
    return render(request, "pages/list.html", context)

def MobileDevicePatterns_view(request):

    obj = MobileDevicePatterns.objects.all()
    context = {
        'object': obj
    }
    
    return render(request, "pages/list.html", context)
    
def MetaAbstractions_view(request):

    obj = MetaAbstractions.objects.all()
    context = {
        'object': obj
    }
    
    return render(request, "pages/list.html", context)

def StandardAbstractions_view(request):

    obj = StandardAbstractions.objects.all()
    context = {
        'object': obj
    }
    
    return render(request, "pages/list.html", context)

def DetailedAbstractions_view(request):

    obj = DetailedAbstractions.objects.all()
    context = {
        'object': obj
    }
    
    return render(request, "pages/list.html", context)


#query id
@csrf_exempt
def id_view(request):
    
    idval = "null"
    idval = request.POST.get("id_query")
    
    obj = DomainsOfAttack.objects.filter(id=idval)
    
    if obj.exists():
        context = {
           'object': obj
        }
        return render(request, "pages/id_results.html", context)
    else:
        return render(request, "pages/id_results.html", {})
    
    
#query ParentOf
@csrf_exempt
def parent_view(request):

    idval = "null"
    idval = request.POST.get("id_query")
    
    obj = DomainsOfAttack.objects.filter(relatedattackpatterns__contains=":" + idval + "::")
    
    if obj.exists():
        context = {
           'object': obj
        }
        return render(request, "pages/parent_results.html", context)
    else:
        return render(request, "pages/parent_results.html", {})


#query name
@csrf_exempt
def name_view(request):

    name = " "
    name = request.POST.get("name")
    
    obj = DomainsOfAttack.objects.filter(name__icontains=name)
    
    if obj.exists():
        context = {
           'object': obj
        }
        return render(request, "pages/name_results.html", context)
    else:
        return render(request, "pages/name_results.html", {})    