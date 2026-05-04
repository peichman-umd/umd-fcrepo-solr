import pytest

pytestmark = pytest.mark.fcrepo


@pytest.mark.parametrize(
    ('input_text', 'search_term'),
    [
        ('Class|n=0&xywh=0,0,100,100', 'class'),
        ('“Class|n=0&xywh=0,0,100,100', 'class'),
        ('Class”|n=0&xywh=0,0,100,100', 'class'),
        ('“Class”|n=0&xywh=0,0,100,100', 'class'),
    ]
)
def test_strip_punctuation(index, solr, doc_in_results, input_text, search_term):
    doc = index({
        'extracted_text__dps_txt': input_text
    })
    results = solr.search(f'extracted_text__dps_txt:{search_term}')
    assert doc_in_results(doc['id'], results)
