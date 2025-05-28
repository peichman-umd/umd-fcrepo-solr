import os

import pytest


@pytest.fixture()
def solr_endpoint():
    return os.environ.get('SOLR_ENDPOINT_FCREPO', 'http://localhost:8985/solr/fcrepo')
