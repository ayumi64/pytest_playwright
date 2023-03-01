## Start Pytest with the base-url argument. 
pytest --base-url http://localhost:8080

pytest --headed  --browser chromium  test_sample.py


## Running Codegen
playwright codegen demo.playwright.dev/todomvc
playwright codegen http://whatsmyuseragent.org

## RunTest
pytest headed


## 虚拟环境

python3 -m venv ./venv  
source venv/bin/activate