# python-fastapi-data-retrival-app

[![Release](https://img.shields.io/github/v/release/Lishuaijing3/python-fastapi-data-retrival-app)](https://img.shields.io/github/v/release/Lishuaijing3/python-fastapi-data-retrival-app)
[![Build status](https://img.shields.io/github/actions/workflow/status/Lishuaijing3/python-fastapi-data-retrival-app/main.yml?branch=main)](https://github.com/Lishuaijing3/python-fastapi-data-retrival-app/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/Lishuaijing3/python-fastapi-data-retrival-app/branch/main/graph/badge.svg)](https://codecov.io/gh/Lishuaijing3/python-fastapi-data-retrival-app)
[![Commit activity](https://img.shields.io/github/commit-activity/m/Lishuaijing3/python-fastapi-data-retrival-app)](https://img.shields.io/github/commit-activity/m/Lishuaijing3/python-fastapi-data-retrival-app)
[![License](https://img.shields.io/github/license/Lishuaijing3/python-fastapi-data-retrival-app)](https://img.shields.io/github/license/Lishuaijing3/python-fastapi-data-retrival-app)

This project using python fastAPI framwork to retrive data from a databricks workspace (you can customise to similar databases)

- **Github repository**: <https://github.com/Lishuaijing3/python-fastapi-data-retrival-app/>
- **Documentation** <https://Lishuaijing3.github.io/python-fastapi-data-retrival-app/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

``` bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:Lishuaijing3/python-fastapi-data-retrival-app.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with 

```bash
make install
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).


## Run different apps

### Run backend:
``` bash
poetry run uvicorn python_fastapi_data_retrival_app.fastAPI_backend:app --port 8000 --reload 
``` 
To test the backend, using http://127.0.0.1:8000/docs, then you can use post and get methods to interact with the two APIs.

### run dash front end
``` bash
poetry run python python_fastapi_data_retrival_app/dash_frontend.py
``` 
## Releasing a new version



---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).