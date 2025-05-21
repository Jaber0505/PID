from account.models import RoleUser

def role_users_processor(request):
    role_users = RoleUser.objects.select_related('user', 'role') if request.user.is_authenticated else []
    return {"role_users": role_users}
