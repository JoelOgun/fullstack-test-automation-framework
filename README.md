# Fullstack Test Automation Framework (Skeleton)

Tech: Python 3.12 · Pytest · Selenium · Requests · JSON Schema · Dotenv  
Suites: UI (Selenium), API (Requests), DB (optional), Perf (JMeter)

## Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Run (after you add tests)
pytest --env-file config/dev.env -q
pytest -m ui
pytest -m api
