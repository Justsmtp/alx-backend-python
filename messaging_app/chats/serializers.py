from rest_framework import serializers
from .models import User, Conversation, Message


# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Add more fields if needed


# Serializer for the Message model
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp', 'conversation']
        read_only_fields = ['id', 'timestamp']


# Serializer for the Conversation model with nested messages
class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'created_at', 'messages']
