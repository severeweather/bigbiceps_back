from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from datetime import date, datetime

from accounts.models import CustomUser
from social.models import UserSocialProfile


def homepage(request):
    return render(request, 'homepage.html')


@login_required
def plate(request):
    return render(request, 'plate.html')


@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    social_profile = get_object_or_404(UserSocialProfile, owner=user)
    user_follows = request.user.following.filter(following=user)
    count_flwrs = user.followers.count()
    count_flws = user.following.count()
    return render(request, 'profile.html', {"social_profile": social_profile, 
                                            "count_flwrs": count_flwrs, 
                                            "count_flws": count_flws, 
                                            "profile_user": user,
                                            "user_follows": user_follows,
                                            })