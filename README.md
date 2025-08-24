# Testing

```bash
pytest --cov=app --cov-report=html
```

# To run sonar in Docker
COPY sonar-project.properties .
CMD ["sonar-scanner"]