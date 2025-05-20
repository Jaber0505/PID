from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from catalogue.models import Artist
from catalogue.forms import ArtistForm

def index(request):
    artists = Artist.objects.all()
    return render(request, 'artist/index.html', {
        'artists': artists,
        'title': "🧑‍🎤 Artistes"
    })

def show(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, 'artist/show.html', {
        'artist': artist,
        'title': f"👤 L'artiste {artist.first_name} {artist.last_name}"
    })

def create(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Artiste ajouté avec succès.")
            return redirect('catalogue:artist-index')
        else:
            messages.error(request, "❌ Une erreur est survenue. Veuillez vérifier le formulaire.")
    else:
        form = ArtistForm()

    return render(request, 'artist/form.html', {
        'form': form,
        'title': "Ajouter un artiste"
    })

def edit(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)

    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            messages.info(request, "✅ Artiste modifié avec succès.")
            return redirect('catalogue:artist-show', artist.id)
        else:
            messages.error(request, "❌ Une erreur est survenue. Veuillez vérifier le formulaire.")
    else:
        form = ArtistForm(instance=artist)

    return render(request, 'artist/form.html', {
        'form': form,
        'title': f"✏️ Modifier l’artiste : {artist.first_name} {artist.last_name}"
    })

def delete(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)

    if request.method == "POST":
        artist.delete()
        messages.warning(request, "✅ Artiste supprimé.")
        return redirect('catalogue:artist-index')

    return render(request, 'artist/delete.html', {
        'artist': artist,
        'title': f"🗑 Supprimer {artist.first_name} {artist.last_name}"
    })
