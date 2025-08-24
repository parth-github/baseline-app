# Testing

```bash
pytest --cov=app --cov-report=xml
```

# To run sonar in Docker
COPY sonar-project.properties .
CMD ["sonar-scanner"]