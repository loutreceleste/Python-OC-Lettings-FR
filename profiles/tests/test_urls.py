import pytest
from django.contrib.auth.models import User

from django.urls import reverse, resolve
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_url():
    user = User.objects.create_user(username='4meRomance', password='password')
    Profile.objects.create(id=1, favorite_city="Marseille", user_id=user.id)

    path = reverse('profiles:profile', kwargs={'username': user.username})

    assert path == "/profiles/4meRomance/"
    assert resolve(path).view_name == 'profiles:profile'
