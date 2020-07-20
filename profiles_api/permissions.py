from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is editing their own profile and not someone else's profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        # print(f'request.method = {request.method}')
        # attrs = vars(obj)
        # for i in attrs.values():
        #     print(f'object: {i}')

        return obj.id == request.user.id




