import os
from uuid import uuid4

import pytest
from pysolr import Solr


def _index_doc(solr, doc):
    uuid = str(uuid4())
    solr.add([{'id': uuid, **doc}])
    solr.commit()
    results = solr.search(f'id:{uuid}')
    return uuid, results


def _cleanup(solr, uuid):
    # clean up after ourselves
    solr.delete(id=uuid)
    solr.commit()


@pytest.fixture()
def solr_endpoint():
    return os.environ.get('SOLR_ENDPOINT', 'http://localhost:8983/solr/fedora4')


@pytest.fixture()
def solr(solr_endpoint):
    return Solr(solr_endpoint)


@pytest.mark.parametrize(
    ('input_date', 'output_date'),
    [
        ('2012', '2012-01-01T00:00:00Z'),
        ('~2012', '2012-01-01T00:00:00Z'),
        ('2012~', '2012-01-01T00:00:00Z'),
        ('?2012', '2012-01-01T00:00:00Z'),
        ('2012?', '2012-01-01T00:00:00Z'),
        ('%2012', '2012-01-01T00:00:00Z'),
        ('2012%', '2012-01-01T00:00:00Z'),
        ('211X', '2110-01-01T00:00:00Z'),
        ('21XX', '2100-01-01T00:00:00Z'),
        ('2XXX', '2000-01-01T00:00:00Z'),
    ]
)
def test_date_field_year_only(solr, input_date, output_date):
    uuid, results = _index_doc(solr, {'date': input_date})
    assert results.docs[0]['date'] == output_date
    _cleanup(solr, uuid)


@pytest.mark.parametrize(
    ('input_date', 'output_date'),
    [
        ('2012-04', '2012-04-01T00:00:00Z'),
        ('~2012-04', '2012-04-01T00:00:00Z'),
        ('2012~-04', '2012-04-01T00:00:00Z'),
        ('2012-~04', '2012-04-01T00:00:00Z'),
        ('2012-04~', '2012-04-01T00:00:00Z'),
        ('?2012-04', '2012-04-01T00:00:00Z'),
        ('2012?-04', '2012-04-01T00:00:00Z'),
        ('2012-?04', '2012-04-01T00:00:00Z'),
        ('2012-04?', '2012-04-01T00:00:00Z'),
        ('%2012-04', '2012-04-01T00:00:00Z'),
        ('2012%-04', '2012-04-01T00:00:00Z'),
        ('2012-%04', '2012-04-01T00:00:00Z'),
        ('2012-04%', '2012-04-01T00:00:00Z'),
        ('2112-0X', '2112-01-01T00:00:00Z'),
        ('2112-1X', '2112-10-01T00:00:00Z'),
        ('211X-0X', '2110-01-01T00:00:00Z'),
        ('211X-1X', '2110-10-01T00:00:00Z'),
        ('21XX-0X', '2100-01-01T00:00:00Z'),
        ('21XX-1X', '2100-10-01T00:00:00Z'),
        ('2XXX-0X', '2000-01-01T00:00:00Z'),
        ('2XXX-1X', '2000-10-01T00:00:00Z'),
    ]
)
def test_date_field_year_month(solr, input_date, output_date):
    uuid, results = _index_doc(solr, {'date': input_date})
    assert results.docs[0]['date'] == output_date
    _cleanup(solr, uuid)


@pytest.mark.parametrize(
    ('input_date', 'output_date'),
    [
        ('2012-04-26', '2012-04-26T00:00:00Z'),
        ('~2012-04-26', '2012-04-26T00:00:00Z'),
        ('2012~-04-26', '2012-04-26T00:00:00Z'),
        ('2012-~04-26', '2012-04-26T00:00:00Z'),
        ('2012-04~-26', '2012-04-26T00:00:00Z'),
        ('2012-04-~26', '2012-04-26T00:00:00Z'),
        ('2012-04-26~', '2012-04-26T00:00:00Z'),
        ('?2012-04-26', '2012-04-26T00:00:00Z'),
        ('2012?-04-26', '2012-04-26T00:00:00Z'),
        ('2012-?04-26', '2012-04-26T00:00:00Z'),
        ('2012-04?-26', '2012-04-26T00:00:00Z'),
        ('2012-04-?26', '2012-04-26T00:00:00Z'),
        ('2012-04-26?', '2012-04-26T00:00:00Z'),
        ('%2012-04-26', '2012-04-26T00:00:00Z'),
        ('2012%-04-26', '2012-04-26T00:00:00Z'),
        ('2012-%04-26', '2012-04-26T00:00:00Z'),
        ('2012-04%-26', '2012-04-26T00:00:00Z'),
        ('2012-04-%26', '2012-04-26T00:00:00Z'),
        ('2012-04-26%', '2012-04-26T00:00:00Z'),
        # 2112-*-*
        ('2112-04-0X', '2112-04-01T00:00:00Z'),
        ('2112-04-1X', '2112-04-10T00:00:00Z'),
        ('2112-04-2X', '2112-04-20T00:00:00Z'),
        ('2112-04-3X', '2112-04-30T00:00:00Z'),
        ('2112-0X-13', '2112-01-13T00:00:00Z'),
        ('2112-0X-0X', '2112-01-01T00:00:00Z'),
        ('2112-0X-1X', '2112-01-10T00:00:00Z'),
        ('2112-0X-2X', '2112-01-20T00:00:00Z'),
        ('2112-0X-3X', '2112-01-30T00:00:00Z'),
        ('2112-1X-13', '2112-10-13T00:00:00Z'),
        ('2112-1X-0X', '2112-10-01T00:00:00Z'),
        ('2112-1X-1X', '2112-10-10T00:00:00Z'),
        ('2112-1X-2X', '2112-10-20T00:00:00Z'),
        ('2112-1X-3X', '2112-10-30T00:00:00Z'),
        # 211X-*-*
        ('211X-0X-13', '2110-01-13T00:00:00Z'),
        ('211X-0X-0X', '2110-01-01T00:00:00Z'),
        ('211X-0X-1X', '2110-01-10T00:00:00Z'),
        ('211X-0X-2X', '2110-01-20T00:00:00Z'),
        ('211X-0X-3X', '2110-01-30T00:00:00Z'),
        ('211X-1X-13', '2110-10-13T00:00:00Z'),
        ('211X-1X-0X', '2110-10-01T00:00:00Z'),
        ('211X-1X-1X', '2110-10-10T00:00:00Z'),
        ('211X-1X-2X', '2110-10-20T00:00:00Z'),
        ('211X-1X-3X', '2110-10-30T00:00:00Z'),
        # 21XX-*-*
        ('21XX-0X-13', '2100-01-13T00:00:00Z'),
        ('21XX-0X-0X', '2100-01-01T00:00:00Z'),
        ('21XX-0X-1X', '2100-01-10T00:00:00Z'),
        ('21XX-0X-2X', '2100-01-20T00:00:00Z'),
        ('21XX-0X-3X', '2100-01-30T00:00:00Z'),
        ('21XX-1X-13', '2100-10-13T00:00:00Z'),
        ('21XX-1X-0X', '2100-10-01T00:00:00Z'),
        ('21XX-1X-1X', '2100-10-10T00:00:00Z'),
        ('21XX-1X-2X', '2100-10-20T00:00:00Z'),
        ('21XX-1X-3X', '2100-10-30T00:00:00Z'),
        # 2XXX-*-*
        ('2XXX-0X-13', '2000-01-13T00:00:00Z'),
        ('2XXX-0X-0X', '2000-01-01T00:00:00Z'),
        ('2XXX-0X-1X', '2000-01-10T00:00:00Z'),
        ('2XXX-0X-2X', '2000-01-20T00:00:00Z'),
        ('2XXX-0X-3X', '2000-01-30T00:00:00Z'),
        ('2XXX-1X-13', '2000-10-13T00:00:00Z'),
        ('2XXX-1X-0X', '2000-10-01T00:00:00Z'),
        ('2XXX-1X-1X', '2000-10-10T00:00:00Z'),
        ('2XXX-1X-2X', '2000-10-20T00:00:00Z'),
        ('2XXX-1X-3X', '2000-10-30T00:00:00Z'),
    ]
)
def test_date_field_year_month_day(solr, input_date, output_date):
    uuid, results = _index_doc(solr, {'date': input_date})
    assert results.docs[0]['date'] == output_date
    _cleanup(solr, uuid)


@pytest.mark.parametrize(
    ('input_date', 'output_date'),
    [
        ('2012/', '2012-01-01T00:00:00Z'),
        ('/2012', '2012-01-01T00:00:00Z'),
        ('2012/..', '2012-01-01T00:00:00Z'),
        ('../2012', '2012-01-01T00:00:00Z'),
    ]
)
def test_date_field_interval(solr, input_date, output_date):
    uuid, results = _index_doc(solr, {'date': input_date})
    assert results.docs[0]['date'] == output_date
    _cleanup(solr, uuid)


@pytest.mark.parametrize(
    ('input_date', 'output_date'),
    [
        ('[2012-04-26,2012-05]', '2012-04-26T00:00:00Z'),
        ('[2012..]', '2012-01-01T00:00:00Z'),
        ('[..2012]', '2012-01-01T00:00:00Z'),
    ]
)
def test_date_field_set(solr, input_date, output_date):
    uuid, results = _index_doc(solr, {'date': input_date})
    assert results.docs[0]['date'] == output_date
    _cleanup(solr, uuid)


@pytest.mark.parametrize(
    ('input_date', 'output_date'),
    [
        # Spring --> March 1
        ('2012-21', '2012-03-01T00:00:00Z'),
        # Summer --> June 1
        ('2012-22', '2012-06-01T00:00:00Z'),
        # Autumn --> September 1
        ('2012-23', '2012-09-01T00:00:00Z'),
        # Winter --> December 1
        ('2012-24', '2012-12-01T00:00:00Z'),
    ]
)
def test_date_field_seasons(solr, input_date, output_date):
    uuid, results = _index_doc(solr, {'date': input_date})
    assert results.docs[0]['date'] == output_date
    _cleanup(solr, uuid)
