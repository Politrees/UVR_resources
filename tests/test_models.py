import pytest
import json
import requests
from urllib.parse import unquote, urlparse
from pathlib import Path


def load_model_links():
    with open('UVR_resources/model_list_links.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def collect_urls(data):
    """Рекурсивно собирает все URL из JSON структуры без изменений"""
    urls = []
    if isinstance(data, dict):
        for value in data.values():
            urls.extend(collect_urls(value))
    elif isinstance(data, list):
        for item in data:
            urls.extend(collect_urls(item))
    elif isinstance(data, str) and data.startswith(('http://', 'https://')):
        urls.append(data)
    return urls


def extract_filename(url):
    """Извлекает оригинальное имя файла из URL без изменений"""
    path = unquote(urlparse(url).path)
    return Path(path).name


def collect_expected_filenames(data):
    """Собирает точные имена файлов из JSON"""
    filenames = set()

    def _recursive_collect(item):
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str) and value.startswith(('http://', 'https://')):
                    filenames.add(key)
                _recursive_collect(value)
        elif isinstance(item, list):
            for element in item:
                _recursive_collect(element)

    _recursive_collect(data)
    return filenames


@pytest.fixture(scope="module")
def expected_filenames():
    return collect_expected_filenames(load_model_links())


@pytest.mark.parametrize("url", collect_urls(load_model_links()), ids=None)
def test_url_and_filename_validity(url, expected_filenames):
    try:
        # 1. Проверка доступности URL
        response = requests.head(url, allow_redirects=True, timeout=15)
        assert response.status_code == 200, f"Status code {response.status_code}"

        # 2. Извлекаем оригинальное имя файла из URL
        actual_filename = extract_filename(url)

        # 3. Проверяем точное соответствие имени файла
        assert actual_filename in expected_filenames, (
            f"Filename '{actual_filename}' not found in model list. "
            f"URL: {url}"
        )

        # 4. Проверка Content-Type
        content_type = response.headers.get('Content-Type', '')
        assert 'text/html' not in content_type, "HTML response instead of file"

    except RequestException as e:
        pytest.fail(f"Request failed: {str(e)}")
