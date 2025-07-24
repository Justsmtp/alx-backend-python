# messaging_app/chats/permissions.py
from rest_framework import permissions

class IsOwnerOrParticipant(permissions.BasePermission):
    """
    Custom permission to only allow users to access their own messages or conversations.
    """

    def has_object_permission(self, request, view, obj):
        # Customize based on your model structure
        return obj.sender == request.user or obj.receiver == request.user
