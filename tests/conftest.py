import os
from uuid import uuid4

import pytest
from pysolr import Solr


@pytest.fixture()
def solr_endpoint():
    return os.environ.get('SOLR_ENDPOINT', 'http://localhost:8983/solr/fedora4')


@pytest.fixture()
def solr(solr_endpoint):
    return Solr(solr_endpoint)


@pytest.fixture
def index(solr):
    """
    Fixture factory for creating Solr documents, and then cleaning them up
    after the test is complete.
    """

    uuids = []

    def _index(fields):
        uuid = str(uuid4())
        uuids.append(uuid)
        solr.add([{'id': uuid, **fields}])
        solr.commit()
        return solr.search(f'id:{uuid}').docs[0]

    yield _index

    # clean up after ourselves
    solr.delete(id=uuids)
    solr.commit()
