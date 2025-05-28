import pytest

pytestmark = pytest.mark.fedora4


@pytest.mark.parametrize(
    ('input_handle', 'output_handle'),
    [
        ('hdl:1903.1/12345', '1903.1/12345'),
        # no prefix should be a no-op
        ('1903.1/12345', '1903.1/12345'),
        # empty string should be a no-op
        ('', ''),
        # non-hdl prefix should be a no-op
        ('urn:isbn:1234566789', 'urn:isbn:1234566789'),
        # only remove "hdl:" at the beginning
        ('hdl:1903.1/hdl:bar', '1903.1/hdl:bar'),
    ]
)
def test_remove_hdl_prefix(index, input_handle, output_handle):
    doc = index({'handle': input_handle})
    assert doc['handle'] == output_handle
