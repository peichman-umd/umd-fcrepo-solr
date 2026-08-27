# umd-fcrepo-solr

Solr cores for the UMD Libraries Fedora indexes

## Cores

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

The tests require a running Solr instance. By default, it assumes the
endpoint URL is:

* <http://localhost:8985/solr/fcrepo> for the **fcrepo** core

This can be changed by setting the environment variable `SOLR_ENDPOINT_{CORE_NAME}`.

**NOTE:** After the removal of the fedora4 core there should just be `SOLR_ENDPOINT_FCREPO`

```zsh
# run all tests with the default endpoint
pytest

# run just the fcrepo tests
pytest -m fcrepo

# run all tests but use a custom endpoint for the fcrepo core
SOLR_ENDPOINT_FCREPO=http://localhost:18985/solr/fcrepo pytest
```

## License

See the [LICENSE](LICENSE) file for license rights and limitations (Apache 2.0).

[pytest]: https://pypi.org/project/pytest/
