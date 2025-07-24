from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow only authenticated users who are participants in a conversation
    to send, view, update, and delete messages.
    """

    def has_permission(self, request, view):
        # Allow only authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check participant for Conversation or Message
        user = request.user

        # Handle Conversation object
        if hasattr(obj, 'participants'):
            return user in obj.participants.all()

        # Handle Message object by checking conversation participants
        if hasattr(obj, 'conversation'):
            is_participant = user in obj.conversation.participants.all()

            # Restrict modifying methods to participants only
            if request.method in ['PUT', 'PATCH', 'DELETE']:
                return is_participant

            # Allow safe methods (GET, HEAD, OPTIONS) to participants
            return is_participant

        return False
