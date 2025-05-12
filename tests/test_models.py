import pytest
import json
import requests
from urllib.parse import unquote, urlparse
from pathlib import Path


def load_model_links():
    with open('UVR_resources/model_list_links.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_filename(url):
    """Достает оригинальное имя файла из URL"""
    path = unquote(urlparse(url).path)
    return Path(path).name


def collect_expected_filenames(data):
    """Собирает все имена файлов из JSON структуры"""
    filenames = set()
    
    def _recursive_collect(item):
        if isinstance(item, dict):
            for key, value in item.items():
                if key.endswith(('.th', '.pth', '.ckpt', '.onnx', '.yaml')):
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


@pytest.mark.parametrize("url", collect_urls(load_model_links()))
def test_url_and_filename_validity(url, expected_filenames):
    try:
        # 1. Проверка доступности URL
        response = requests.head(url, allow_redirects=True, timeout=15)
        assert response.status_code == 200, f"Status code {response.status_code}"

        # 2. Извлекаем имя файла из URL
        actual_filename = extract_filename(url)
        
        # 3. Проверяем, что имя файла существует в expected_filenames
        assert actual_filename in expected_filenames, \
            f"Filename {actual_filename} not found in model list"

        # 4. Проверка Content-Type
        content_type = response.headers.get('Content-Type', '')
        assert 'text/html' not in content_type, "HTML response instead of file"

        # 5. Проверка минимального размера для бинарных файлов
        if any(actual_filename.endswith(ext) for ext in ['.th', '.pth', '.ckpt', '.onnx']):
            size = int(response.headers.get('Content-Length', 0))
            assert size > 1024, f"File too small: {size} bytes"

    except RequestException as e:
        pytest.fail(f"Request failed: {str(e)}")
