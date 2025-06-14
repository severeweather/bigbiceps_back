from django.db import models

class UserSocialProfile(models.Model):
    owner = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=False)
    pfp = models.ImageField(upload_to="pfps/", blank=True, null=True)


class Follow(models.Model):
    follower = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name="followers")

    class Meta:
        unique_together = ('follower', 'following')