#!/usr/bin/env bash
source venv/bin/activate
echo "-> Installing dependencies"
python -m pip install --upgrade pip
python -m playwright install
pip install -r requirements.txt

echo "-> Start tests"

pytest --headed  tests/login/test_login_demo.py

echo "-> Test finished"

echo "-> Open report"
open pytest_html_report.html