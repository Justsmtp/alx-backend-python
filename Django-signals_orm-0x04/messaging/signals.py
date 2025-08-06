from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Editing existing message
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                # Save history before change
                MessageHistory.objects.create(
                    original_message=old_message,
                    old_content=old_message.content
                )
                # Mark as edited
                instance.edited = True
        except Message.DoesNotExist:
            pass  # It's a new message, not an edit
