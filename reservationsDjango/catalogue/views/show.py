from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from catalogue.models.show import Show
from catalogue.forms.show_form import ShowForm

def index(request):
    shows = Show.objects.all()
    return render(request, "show/index.html", {
        "title": "🎬 Films",
        "shows": shows,
    })

def show(request, slug):
    show = get_object_or_404(Show, slug=slug)
    representations = show.representations.all()

    return render(request, "show/show.html", {
        "title": f"🎭 {show.title}",
        "show": show,
        "representations": representations,
    })

def create(request):
    if request.method == "POST":
        form = ShowForm(request.POST)
        if form.is_valid():
            show = form.save()
            messages.success(request, "✅ Spectacle ajouté.")
            return redirect("catalogue:show-show", show.slug)
        messages.error(request, "❌ Erreur lors de la création.")
    else:
        form = ShowForm()

    return render(request, "show/form.html", {
        "form": form,
        "title": "➕ Ajouter un spectacle",
    })

def edit(request, slug):
    show_obj = get_object_or_404(Show, slug=slug)

    if request.method == "POST":
        form = ShowForm(request.POST, instance=show_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Spectacle modifié avec succès.")
            return redirect("catalogue:show-show", form.instance.slug)
        messages.error(request, "❌ Erreur lors de la modification.")
    else:
        form = ShowForm(instance=show_obj)

    return render(request, "show/form.html", {
        "form": form,
        "title": f"✏️ Modifier : {show_obj.title}",
    })

def delete(request, slug):
    show_obj = get_object_or_404(Show, slug=slug)

    if request.method == "POST":
        show_obj.delete()
        messages.success(request, "🗑 Spectacle supprimé avec succès.")
        return redirect("catalogue:show-index")

    return render(request, "show/delete.html", {
        "show": show_obj,
        "title": f"🗑 Supprimer : {show_obj.title}",
    })
