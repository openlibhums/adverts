from django.shortcuts import render

from plugins.adverts import forms


def manager(request):
    form = forms.AdvertForm()

    template = 'adverts/manager.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
