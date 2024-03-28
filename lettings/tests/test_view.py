import pytest

from django.test import Client
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_view():
    client = Client()
    address = Address.objects.create(id=1, number=30, street='Oratoire', city='Marseille', state='France', zip_code='13009', country_iso_code='FRA')
    letting = Letting.objects.create(id=1, title="Marseille", address_id=address.id)

    path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<p>Marseille, France 13009</p>"

    assert response.status_code == 200
    assert expected_content in content
