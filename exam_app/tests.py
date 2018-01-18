from django.test import TestCase
import pytest


@pytest.mark.django_db
def test_category(client):
    response = client.get('/api/v1/products/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_user(client):
    response = client.get('/api/v1/users/')
    assert response.status_code == 405


@pytest.mark.django_db
def test_product(client):
    response = client.get('/api/v1/order/')
    assert response.status_code == 200se.status_code == 200