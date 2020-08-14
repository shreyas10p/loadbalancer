# from loadbalancer import urls
import pytest
from django.urls import reverse
import json
from loadbalancer.server import Server
import asyncio
from concurrent.futures import ThreadPoolExecutor
# @pytest.fixture
# def client():
#     with test_client() as client:
#         yield client

executor = ThreadPoolExecutor(max_workers = 6)

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

@pytest.mark.django_db
def test_multiple_requests(client):
    result_list = []
    url = reverse('router')
    host = 'www.hostaddress1.com'
    loop = asyncio.get_event_loop()
    result_list = loop.run_until_complete(fetch_urls_coop(client,url,loop))
    loop.close()
    for result in result_list:
        result = json.loads(result.content.decode('utf-8'))
        assert result['status_code'] == 200



async def fetch_urls_coop(client,url,loop):
    gether_list = []
    for i in range(5):
        gether_list.append(loop.run_in_executor(executor,lambda:client.get(url,HTTP_HOST='www.hostaddress1.com')))
    return await asyncio.gather(*gether_list)
