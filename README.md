# Agent Test

## Installation

### Required

- Python >= 3.13.0
- Poetry

### Recommended
- Pyenv

### Optional

Execute the following command to install dependencies in project rather than venv
path. This prevents configuring interpeter path in VSCode.

```bash
poetry config virtualenvs.in-project true --local
```

Remove the ```--local``` flag to set this setting as default.

### Install dependencies
Create virtual environment and install all project dependencies.

```bash
poetry install
```

## Usage

Start a web server and expose the API

### Production

```bash
poetry run fastapi run
```

### Development

```bash
poetry run fastapi dev
```

## Contributing

Use poetry for managing the virtual environment and the dependencies. Don't use ```venv```
nor ```pip```.

| Action | Command |
| ------ | ------- |
| Install all dependencies in your virtual environemnt | ```poetry install```
| Add dependency to project | ```poetry add <package_name>```
| Remove dependency from project | ```poetry remove <package_name>```
| Run script or executable | ```poetry run <script_name> <script_args>```
| Show information about virtual environment | ```poetry env info```

## Update packages

Update poetry:

```bash
poetry self update
```

Update dependencies:
```bash
poetry update
```
