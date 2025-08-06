from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse

User = get_user_model()


@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return HttpResponse("Your account and all related data have been deleted.")
    return HttpResponse("Invalid request", status=400)
