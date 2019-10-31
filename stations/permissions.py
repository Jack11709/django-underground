from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
    '''
    Object level permissions to only allow owner of an object to edit it
    '''

    def has_object_permission(self, request, view, obj):
        # return true for safe methods, this is our GET requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise we return an evaluation if the objects user field and the user attached to the request (gathered from the token used)
        return obj.owner == request.user

        