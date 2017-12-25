from django.shortcuts import render, get_object_or_404, redirect
from bitlyclone.models import ShortUrl
from bitlyclone.form import ShortUrlForm

def liste(request):
    """Affichage des redirections"""

    shorturl_list = ShortUrl.objects.order_by('-date')

    return render(request, 'bitlyclone/liste.html', locals())

def new(request):
    """Ajout de redirection"""
    if request.method == "POST":
        form = ShortUrlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste)
    else:
        form = ShortUrlForm()

    return render(request, 'bitlyclone/new.html', {'form': form})

def redirection(request,code):
    """Redirection vers l'URL enregistrée"""

    shorturl = get_object_or_404(ShortUrl,code=code)
    shorturl.nb_access += 1
    shorturl.save()

    return redirect(shorturl.url)
# Create your views here.
