# Dramatiq-Mongodb Broker and Results Backend for Dramatiq

| :exclamation: _WARNING_ This is very early beta software that has not yet been proven to work. :exclamation: |
| ------------------------------------------------------------------------------------------------------------ |

![CI/CD Pipeline](https://img.shields.io/github/actions/workflow/status/obscuritylabs/dramatiq-mongodb/ci-cd.yaml)

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
poetry run pre-commit install --install-hooks -t pre-commit -t commit-msg
```

### Run code quality checks locally

All code quality checks are performed using the Makefile at the root of the repository. You can execute individual steps by name or execute all steps by omitting a target using `make` or specifying `make all`:

```shell
make all
```

If you want to purge the repo of all ignore files include the embedded virtual environment then run all tests in a fresh environment you can run:

```shell
make clean all
```

Changelog and semantic version are automated using [Semantic-Release](https://python-semantic-release.readthedocs.io/en/latest/) during the CD process. To accomplish this, this repository makes heavy use of [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), thought this isn't strictly enforced on the server side at this time until 1.0 is released, but the githooks will lint your commits.

### Start a local MongoDB

```shell
docker run -d -p 27017:27017 --name mongo -e MONGO_INITDB_ROOT_USERNAME=username -e MONGO_INITDB_ROOT_PASSWORD=password mongo
```

Once the mongodb server is up and running you can create a pymongo client and pass it either into a MongoDBBroker or a MongoDBBackend to test the code locally. Otherwise everything should behave in accordance with the documentation for [Dramatiq](https://dramatiq.io/).
