from rest_framework import permissions
from .models import Conversation

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to participants of a conversation.
    """

    def has_permission(self, request, view):
        # Require the user to be authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Ensure the user is part of the conversation
        if hasattr(obj, 'conversation'):
            return request.user in obj.conversation.participants.all()
        return False
