from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from catalogue.forms.review_form import ReviewForm
from catalogue.models.review import Review
from catalogue.models.representation import Representation

@login_required
def create(request, representation_id):
    representation = get_object_or_404(Representation, pk=representation_id)

    if Review.objects.filter(user=request.user, representation=representation).exists():
        messages.info(request, "ℹ️ Vous avez déjà laissé un avis pour cette représentation.")
        return redirect("catalogue:representation-show", representation_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.representation = representation
            review.save()
            messages.success(request, "✅ Avis ajouté avec succès.")
            return redirect("catalogue:representation-show", representation_id)
        messages.error(request, "❌ Erreur lors de la soumission de l’avis.")
    else:
        form = ReviewForm()

    return render(request, "review/form.html", {
        "form": form,
        "title": "📝 Donner un avis",
        "representation": representation,
    })

@login_required
def edit(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Avis modifié.")
            return redirect("catalogue:representation-show", review.representation.id)
        messages.error(request, "❌ Erreur lors de la modification.")
    else:
        form = ReviewForm(instance=review)

    return render(request, "review/form.html", {
        "form": form,
        "title": "✏️ Modifier mon avis",
        "representation": review.representation,
    })

@login_required
def delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method == "POST":
        representation_id = review.representation.id
        review.delete()
        messages.success(request, "🗑 Avis supprimé.")
        return redirect("catalogue:representation-show", representation_id)

    return render(request, "review/delete.html", {
        "review": review,
        "title": "🗑 Supprimer l’avis",
    })
