import os, pytest
from dotenv import load_dotenv

def pytest_addoption(parser):
    parser.addoption("--env-file", default="config/dev.env")
    parser.addoption("--browser", default="chrome", choices=["chrome","firefox"])
    parser.addoption("--headed", action="store_true")

@pytest.fixture(scope="session", autouse=True)
def _load_env(request):
    env_file = request.config.getoption("--env-file")
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Env file not found: {env_file}")
    load_dotenv(env_file)

@pytest.fixture(scope="session")
def ui_base_url():
    url = os.getenv("UI_BASE_URL")
    if not url: pytest.skip("UI_BASE_URL not set")
    return url

@pytest.fixture(scope="session")
def api_base_url():
    url = os.getenv("API_BASE_URL")
    if not url: pytest.skip("API_BASE_URL not set")
    return url
