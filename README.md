# Testing

# RUN pytest --cov=app --cov-report=xml
# To run with sonar
COPY sonar-project.properties .
CMD ["sonar-scanner"]