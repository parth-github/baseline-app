test:
	poetry run pytest --cov=src --cov-report=xml

sonar: test
	sonar-scanner
