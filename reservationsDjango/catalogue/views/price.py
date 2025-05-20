from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from catalogue.models import Price
from catalogue.forms import PriceForm

def index(request):
    prices = Price.objects.all()
    return render(request, "price/index.html", {
        "prices": prices,
        "title": "Liste des tarifs"
    })

def show(request, price_id):
    price = get_object_or_404(Price, pk=price_id)
    return render(request, "price/show.html", {
        "title": f"Tarif : {price.price} €",
        "price": price,
    })

def create(request):
    if request.method == "POST":
        form = PriceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Tarif créé avec succès.")
            return redirect("catalogue:price-index")
        messages.error(request, "❌ Erreur lors de la création.")
    else:
        form = PriceForm()

    return render(request, "price/form.html", {
        "form": form,
        "title": "➕ Ajouter un tarif"
    })

def edit(request, price_id):
    price = get_object_or_404(Price, pk=price_id)
    if request.method == "POST":
        form = PriceForm(request.POST, instance=price)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Tarif modifié.")
            return redirect("catalogue:price-index")
        messages.error(request, "❌ Erreur lors de la modification.")
    else:
        form = PriceForm(instance=price)

    return render(request, "price/form.html", {
        "form": form,
        "title": f"✏️ Modifier : {price}"
    })

def delete(request, price_id):
    price = get_object_or_404(Price, pk=price_id)
    if request.method == "POST":
        price.delete()
        messages.success(request, "🗑 Tarif supprimé.")
        return redirect("catalogue:price-index")

    return render(request, "price/delete.html", {
        "price": price,
        "title": f"🗑 Supprimer : {price}"
    })
