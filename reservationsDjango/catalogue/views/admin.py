from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST 
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from catalogue.models.review import Review
from account.roles import RoleUser,Role

User = get_user_model()


@staff_member_required
def dashboard(request):
    users = User.objects.all()
    reviews = Review.objects.all()
    role_users = RoleUser.objects.select_related('user', 'role')
    roles = Role.objects.all()

    return render(request, "admin/dashboard.html", {
        "title": "📊 Tableau de bord Admin",
        "users": users,
        "reviews": reviews,
        "role_users": role_users,
        "roles": roles,
    })

@staff_member_required
@require_POST
def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if not user.is_superuser:
        user.delete()
    return redirect("catalogue:admin-dashboard")

@staff_member_required
@require_POST
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect("catalogue:admin-dashboard")


@staff_member_required
@require_POST
def create_role(request):
    name = request.POST.get("name", "").strip()
    if name:
        Role.objects.get_or_create(name=name)
    return redirect("catalogue:admin-dashboard")

@staff_member_required
@require_POST
def delete_role(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    role.delete()
    return redirect("catalogue:admin-dashboard")

@staff_member_required
@require_POST
def assign_role_to_user(request):
    user_id = request.POST.get("user_id")
    role_id = request.POST.get("role_id")

    if user_id and role_id:
        user = get_object_or_404(User, pk=user_id)
        role = get_object_or_404(Role, pk=role_id)

        # Évite les doublons
        RoleUser.objects.get_or_create(user=user, role=role)

    return redirect("catalogue:admin-dashboard")
