from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from catalogue.models.location import Location
from catalogue.forms.location_form import LocationForm
from django.db.models import ProtectedError, RestrictedError

def index(request):
    locations = Location.objects.select_related("locality").all()
    return render(request, "location/index.html", {
        "title": "Liste des lieux",
        "locations": locations,
    })

def show(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    return render(request, "location/show.html", {
        "title": f"Fiche lieu : {location}",
        "location": location,
    })

def create(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Lieu ajouté avec succès.")
            return redirect("catalogue:location-index")
        messages.error(request, "❌ Erreur lors de la création.")
    else:
        form = LocationForm()

    return render(request, "location/form.html", {
        "form": form,
        "title": "➕ Ajouter un lieu",
    })

def edit(request, location_id):
    location = get_object_or_404(Location, pk=location_id)

    if request.method == "POST":
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Lieu modifié avec succès.")
            return redirect("catalogue:location-show", form.instance.id)
        messages.error(request, "❌ Erreur lors de la modification.")
    else:
        form = LocationForm(instance=location)

    return render(request, "location/form.html", {
        "form": form,
        "title": f"✏️ Modifier : {location}",
    })

def delete(request, location_id):
    location = get_object_or_404(Location, pk=location_id)

    if request.method == "POST":
        try:
            location.delete()
            messages.success(request, "🗑 Lieu supprimé avec succès.")
            return redirect("catalogue:location-index")
        except (ProtectedError, RestrictedError):
            messages.error(request, "❌ Ce lieu est utilisé dans une représentation. Suppression impossible.")
            return redirect("catalogue:location-show", location.id)

    return render(request, "location/delete.html", {
        "location": location,
        "title": f"🗑 Supprimer : {location}",
    })
