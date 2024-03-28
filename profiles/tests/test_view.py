import pytest

from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_view():
    client = Client()
    user = User.objects.create_user(username='4meRomance', password='password', email='edygaram@gmail.com')
    Profile.objects.create(id=1, favorite_city="Marseille", user_id=user.id)

    path = reverse('profiles:profile', kwargs={'username': user.username})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "edygaram@gmail.com"

    assert response.status_code == 200
    assert expected_content in content
