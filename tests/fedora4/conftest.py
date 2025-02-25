import os

import pytest


@pytest.fixture()
def solr_endpoint():
    return os.environ.get('SOLR_ENDPOINT_FEDORA4', 'http://localhost:8983/solr/fedora4')
