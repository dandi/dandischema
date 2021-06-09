import pytest

from ..utils import _ensure_newline, name2title, version2tuple


@pytest.mark.parametrize(
    "name,title",
    [
        ("relatedResource", "Related Resource"),
        ("identifier", "Identifier"),
        ("wasGeneratedBy", "Was Generated by"),
        ("sameAs", "Same as"),
        ("includeInCitation", "Include in Citation"),
        ("anExtraField", "An Extra Field"),
        ("propertyID", "Property ID"),
        ("fieldINeed", "Field I Need"),
        ("needsADatum", "Needs a Datum"),
        ("contentUrl", "Content URL"),
        ("ContactPoint", "Contact Point"),
    ],
)
def test_name2title(name, title):
    assert name2title(name) == title


@pytest.mark.parametrize(
    "ver,error",
    [
        ("ContactPoint", True),
        ("0.1.2", False),
        ("0.12.20", False),
        ("0.1.2a", True),
        ("0.1.2-rc1", True),
    ],
)
def test_version(ver, error):
    if error:
        with pytest.raises(ValueError):
            version2tuple(ver)
    else:
        assert len(version2tuple(ver)) == 3


def test_newline():
    obj = "\n"
    assert _ensure_newline(obj).endswith("\n")
    obj = ""
    assert _ensure_newline(obj).endswith("\n")
