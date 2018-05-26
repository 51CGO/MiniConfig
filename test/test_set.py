import miniconfig
import pytest

def test_single_set():

    d = miniconfig.MiniConfig()
    d["a/b/c"] = 1

    assert d["a"]["b"]["c"] == 1

def test_multi_set():

    d = miniconfig.MiniConfig()
    d["a/b/c"] = 1
    d["a/b/d"] = 2

    assert d["a"]["b"]["c"] == 1
    assert d["a"]["b"]["d"] == 2

def test_separator_is_none():

    d = miniconfig.MiniConfig(separator=None)
    d["a/b/c"] = 1

    assert d["a/b/c"] == 1

def test_another_separator():

    d = miniconfig.MiniConfig(separator="::")
    d["a::b::c"] = 1

    d["a"]["b"]["c"] == 1

def test_path_is_empty():

    d = miniconfig.MiniConfig()
    with pytest.raises(ValueError):
        d[""] = 1

def test_path_is_not_a_string():

    d = miniconfig.MiniConfig()
    with pytest.raises(TypeError):
        d[["a"]] = 1
