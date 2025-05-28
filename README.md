# umd-fcrepo-solr

Solr cores for the UMD Libraries Fedora indexes

## Cores

* [fedora4](fedora4)
* [fcrepo](fcrepo)

## Testing

This repository has a Python [pytest] test suite for testing.

### Installing

```zsh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running

The tests require a running instance of one or more of the Solr images defined
in this repo. By default, it assumes that the endpoint URL is:

* <http://localhost:8983/solr/fedora4> for tests marked for the **fedora4** core
* <http://localhost:8985/solr/fcrepo> for tests marked for the **fcrepo** core

This can be changed by setting the environment variable `SOLR_ENDPOINT_{CORE_NAME}`.

```zsh
# run all tests with the default endpoint
pytest

# run just the fedora4 tests
pytest -m fedora4

# run just the fcrepo tests
pytest -m fcrepo

# run tests for just the fedora4 core with a custom endpoint (e.g., a different port)
SOLR_ENDPOINT_FEDORA4=http://localhost:18983/solr/fedora4 pytest -m fedora4

# run all tests but use a custom endpoint for the fcrepo core
SOLR_ENDPOINT_FCREPO=http://localhost:18985/solr/fcrepo pytest
```

## License

See the [LICENSE](LICENSE) file for license rights and limitations (Apache 2.0).


[pytest]: https://pypi.org/project/pytest/
