# Dramatiq-Mongodb Broker and Results Backend for Dramatiq

| :exclamation: _WARNING_ This is very early beta software that has not yet been proven to work. :exclamation: |
| ------------------------------------------------------------------------------------------------------------ |

![CI/CD Pipeline](https://img.shields.io/github/workflow/status/obscuritylabs/dramatiq-mongodb/CI-CD/main?label=CI/CD)

![Latest SEMVER](https://img.shields.io/github/v/tag/obscuritylabs/dramatiq-mongodb)

## Usage Instructions

## Development Instructions

### Configure development environment

Install Development Dependencies using Poetry:

```shell
poetry install
```

Install githooks to automate quality checks locally:

```shell
poetry run task init
```

### Run code quality checks locally

This project uses [TaskiPy](https://pypi.org/project/taskipy/) as an alternative to a makefile. Also like a makefile some of these commands are composites. For example, `poetry run task lint` is really just a meta task that runs `poetry run task lint_flake8` followed by `poetry run task lint_mypy`. If you need to see which tasks can be run and what they do, you can use the following command:

```shell
poetry run task --list
```

Changelog and semantic version are automated using [Semantic-Release](https://python-semantic-release.readthedocs.io/en/latest/) during the CD process. To accomplish this, this repository makes heavy use of [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), thought this isn't strictly enforced on the server side at this time until 1.0 is released, but the githooks will lint your commits.

### Start a local MongoDB

```shell
docker run -d -p 27017:27017 --name mongo -e MONGO_INITDB_ROOT_USERNAME=username -e MONGO_INITDB_ROOT_PASSWORD=password mongo
```

Once the mongodb server is up and running you can create a pymongo client and pass it either into a MongoDBBroker or a MongoDBBackend to test the code locally. Otherwise everything should behave in accordance with the documentation for [Dramatiq](https://dramatiq.io/).
