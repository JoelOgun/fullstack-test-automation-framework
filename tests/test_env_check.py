import os, pytest

@pytest.fixture(scope="session")
def api_base_url():
    url = os.getenv("API_BASE_URL")
    if not url:
        pytest.skip("API_BASE_URL not set in env")
    return url

def test_env_loaded(api_base_url):
    assert api_base_url.startswith("http")
