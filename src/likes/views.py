from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import RedirectView

from .models import Like

User = get_user_model()


class LikeRedirectView(RedirectView):

    def get(self, *args, **kwargs):
        pending_like = get_object_or_404(User, pk=kwargs["pk"])
        user_like, created = Like.objects.get_or_create(user=self.request.user)
        if pending_like in user_like.liked_users.all():
            user_like.liked_users.remove(pending_like)
        else:
            user_like.liked_users.add(pending_like)
        return redirect("profiles:detail", slug=pending_like.username)
