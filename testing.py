# from loadbalancer import urls
import pytest
from django.urls import reverse
import json

# @pytest.fixture
# def client():
#     with test_client() as client:
#         yield client


@pytest.mark.django_db
def test_host1(client):
    url = reverse('router')
    result = client.get(url,HTTP_HOST='www.hostaddress1.com')
    result = json.loads(result.content.decode('utf-8'))
    assert result['status_code'] == 200

@pytest.mark.django_db
def test_host2(client):
    url = reverse('router')
    result = client.get(url,HTTP_HOST='www.hostaddress2.com')
    result = json.loads(result.content.decode('utf-8'))
    assert result['status_code'] == 200

@pytest.mark.django_db
def test_host3(client):
    url = reverse('router')
    result = client.get(url,HTTP_HOST='www.hostaddress3.com')
    result = json.loads(result.content.decode('utf-8'))
    assert result['status_code'] == 200

@pytest.mark.django_db
def test_path_server_1(client):
    url = reverse('server1-url')
    result = client.get(url)
    result = json.loads(result.content.decode('utf-8'))
    assert result['status_code'] == 200 and result['content']['app'] == 'server1'

@pytest.mark.django_db
def test_path_server_2(client):
    url = reverse('server2-url')
    result = client.get(url)
    result = json.loads(result.content.decode('utf-8'))
    assert result['status_code'] == 200 and result['content']['app'] == 'server2'
