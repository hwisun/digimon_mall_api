from rest_framework import permissions

class IsPurchase(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(view.action in ('purchase', 'purchase_mons'))

class IsSafeMethod(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method and permissions.SAFE_METHODS)