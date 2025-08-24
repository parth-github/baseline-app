# Testing

> test → coverage → quality gate automation 🔥
>
> pytest + coverage + SonarQube/SonarCloud together.


## Run Tests with Coverage

```bash
pytest --cov=app --cov-report=html
# or 
poetry run pytest --cov=app --cov-report=html
```

## Run Sonar-scanner (Dockerfile)

```Dockerfile
FROM sonarsource/sonar-scanner-cli:latest
COPY sonar-project.properties .
CMD ["sonar-scanner"]
```
