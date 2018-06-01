import miniconfig

def test_simple():

    d = miniconfig.MiniConfig()
    d["a"] = 1
    d["b"] = 2
    d["c/d"] = 3
    d["c/e"] = 4
    d["c/f/g"] = 5

    keys = [k for k in d]
    assert sorted(keys) == ["a", "b", "c/d", "c/e", "c/f/g"]

def test_empty():

    d = miniconfig.MiniConfig()
    keys = [k for k in d]
    assert keys == []

def test_branch_empty():

    d = miniconfig.MiniConfig()
    d["a"] = {}
    keys = [k for k in d]
    assert keys == []
