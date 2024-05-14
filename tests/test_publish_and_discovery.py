import pytest

published_type = 'http://vocab.lib.umd.edu/access#Published'
top_level_type = 'http://vocab.lib.umd.edu/model#Item'
hidden_type = 'http://vocab.lib.umd.edu/access#Hidden'

@pytest.mark.parametrize(
    ('rdf_types', 'is_published', 'is_top_level', 'is_hidden', 'is_discoverable'),
    [
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


def test_only_top_level_have_flags(index):
    # Not top-level, should not have the "is_*" flags other than "is_top_level:false"
    doc = index({})
    assert not doc['is_top_level']
    assert 'is_published' not in doc
    assert 'is_hidden' not in doc
    assert 'is_discoverable' not in doc


@pytest.mark.parametrize(
    ('rdf_types', 'publication_status', 'visibility'),
    [
        ([top_level_type], 'Unpublished', 'Visible'),
        ([top_level_type, published_type], 'Published', 'Visible'),
        ([top_level_type, hidden_type], 'Unpublished', 'Hidden'),
        ([top_level_type, published_type, hidden_type], 'Published', 'Hidden'),
    ]
)
def test_publish_and_discovery_facets(index, rdf_types, publication_status, visibility):
    doc = index({'rdf_type': rdf_types})
    assert doc['publication_status'] == publication_status
    assert doc['visibility'] == visibility
