# Run through Poetry

```bash
poetry run pytest --cov=app --cov-report=html
```

# To run sonar in Docker
COPY sonar-project.properties .
CMD ["sonar-scanner"]


## Poetry project creation

```bash
poetry new baseline-app
```

## Poetry configuration

```bash
poetry config --list
```

## Poetry Virtual Environment

```bash
poetry install
poetry env info
poetry env use python3.12
```


## Poetry dependencies

```bash
poetry add pytest pytest-cov
poetry show --tree
```

### Remove poetry packages

```bash
poetry remove <package>

### Remove all unused packages

```bash
poetry remove --unused

### Remove all packages

```bash
poetry remove --all


### Remove all development dependencies
```bash
poetry remove --dev

### Remove all optional dependencies
```bash
poetry remove --optional

### Remove all system dependencies
```bash
poetry remove --system


### Remove virtual environment
```bash
poetry env remove <python_version>

