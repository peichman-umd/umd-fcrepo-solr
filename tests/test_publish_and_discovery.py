import pytest

published_type = 'http://vocab.lib.umd.edu/access#Published'
top_level_type = 'http://vocab.lib.umd.edu/model#Item'
hidden_type = 'http://vocab.lib.umd.edu/access#Hidden'

@pytest.mark.parametrize(
    ('rdf_types', 'is_published', 'is_top_level', 'is_hidden', 'is_discoverable'),
    [
        # Published, but not top-level or hidden
        ([published_type], True, False, False, False),
        # Top level, but not published or hidden
        ([top_level_type], False, True, False, False),
        # Published and top-level, but not hidden, so discoverable
        ([published_type, top_level_type], True, True, False, True),
        # Published, top-level, and hidden, so not discoverable
        ([published_type, top_level_type, hidden_type], True, True, True, False),
    ]
)
def test_publish_and_discovery_flags(index, rdf_types, is_published, is_top_level, is_hidden, is_discoverable):
    doc = index({'rdf_type': rdf_types})
    assert doc['is_published'] == is_published
    assert doc['is_top_level'] == is_top_level
    assert doc['is_hidden'] == is_hidden
    assert doc['is_discoverable'] == is_discoverable


@pytest.mark.parametrize(
    ('rdf_types', 'publication_status', 'visibility'),
    [
        ([], 'Unpublished', 'Visible'),
        ([published_type], 'Published', 'Visible'),
        ([hidden_type], 'Unpublished', 'Hidden'),
        ([published_type, hidden_type], 'Published', 'Hidden'),
    ]
)
def test_publish_and_discovery_facets(index, rdf_types, publication_status, visibility):
    doc = index({'rdf_type': rdf_types})
    assert doc['publication_status'] == publication_status
    assert doc['visibility'] == visibility
