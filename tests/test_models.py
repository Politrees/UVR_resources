import pytest
import json
import requests
from requests.exceptions import RequestException


def load_model_links():
    with open('UVR_resources/model_list_links.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def collect_urls(data):
    urls = []
    if isinstance(data, dict):
        for value in data.values():
            urls.extend(collect_urls(value))
    elif isinstance(data, list):
        for item in data:
            urls.extend(collect_urls(item))
    elif isinstance(data, str) and data.startswith('http'):
        urls.append(data)
    return urls


@pytest.mark.parametrize("url", collect_urls(load_model_links()))
def test_url_availability(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        assert response.status_code == 200, f"URL {url} returned status code {response.status_code}"
    except RequestException as e:
        pytest.fail(f"Request to {url} failed: {str(e)}")
