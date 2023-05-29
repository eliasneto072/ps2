from django.shortcuts import render,redirect,get_object_or_404


from .models import Jogos


def homeView(request):
    jogos = Jogos.objects.order_by('-data')
    context={'jogos':jogos}
    return render(request, 'base.html', context)

def featuresView(request):
    context={}
    return render(request, 'features.html', )
