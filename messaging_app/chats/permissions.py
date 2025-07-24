from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow only participants of a conversation
    to view, update or delete messages.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        # Safe methods like GET are allowed if the user is part of the conversation
        if request.method in permissions.SAFE_METHODS:
            return obj.conversation.participants.filter(id=user.id).exists()

        # Allow PUT, PATCH, DELETE only if user is a participant
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.conversation.participants.filter(id=user.id).exists()

        # Default deny
        return False
