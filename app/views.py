from django.shortcuts import render, get_object_or_404
from .models import User


# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, "users/user_list.html", {"users": users})


def user_details(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, "users/user_details.html", {"user": user})
