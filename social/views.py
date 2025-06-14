from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .forms import UserSocialProfileForm
from .models import Follow
from accounts.models import CustomUser
from social.models import UserSocialProfile


@login_required
@require_POST
def follow_or_unfollow(request, id):
    target_user = get_object_or_404(CustomUser, id=id)
    if request.user == target_user:
        return JsonResponse({"ok": False, "error": "You cannot follow yourself."}, status=403)

    follow = request.user.following.filter(following=target_user)
    if follow.exists():
        follow.delete()
        return JsonResponse({"ok": True}, status=200)

    Follow.objects.create(follower=request.user, following=target_user)
    return JsonResponse({"ok": True}, status=200)

@login_required
def profile_manager(request):
    profile = get_object_or_404(UserSocialProfile, owner=request.user)
    if request.method == "PATCH":
        form = UserSocialProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return JsonResponse({}, status=200)
    elif request.method == "GET":
        form = UserSocialProfileForm(instance=profile)
        return render(request, "edit_social_profile.html", {"form": form})
    

def profile(request, username):
    if request.method == "GET":
        user = get_object_or_404(CustomUser, username=username)
        social_profile = get_object_or_404(UserSocialProfile, owner=user)
        my_page = request.user == user
        context = {
            "my_page": my_page,
            "already_following": user.followers.filter(follower=request.user).exists(),
            "flwrs": user.followers.count(),
            "flwng": user.following.count(),
            "social_profile": social_profile,
            "profile_user": user,
        }
        return render(request, "profile.html", context)
