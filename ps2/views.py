from django.shortcuts import render,redirect,get_object_or_404


from .models import Jogos


def homeView(request):
    jogos = Jogos.objects.order_by('-data')
    context={'jogos':jogos}
    return render(request, 'base.html', context)

def jogosView(request, id):
   jogos = Jogos.objects.filter(id=id)
   context = {'jogos': jogos}
   return render(request, 'jogos.html', context)
