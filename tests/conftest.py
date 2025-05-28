from uuid import uuid4

import pytest
from pysolr import Solr


@pytest.fixture()
def solr(solr_endpoint):
    # solr_endpoint should be defined in a per-core conftest.py file
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
        doc = {'id': uuid, **fields}
        solr.add([doc])
        solr.commit()
        return solr.search('{!term f=id v=$uuid}', uuid=doc['id']).docs[0]

    yield _index

    # clean up after ourselves
    solr.delete(id=uuids)
    solr.commit()
