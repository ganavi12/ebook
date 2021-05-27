from rest_framework import permissions


# class IsAuthenticatedOrReadOnly(permissions.IsAdminUser):
#     is_admin = super().has_permission(request, view)
#     return  request.method in permissions.SAFE_METHODS OR is_admin