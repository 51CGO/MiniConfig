import miniconfig

def test_len():

    d = miniconfig.MiniConfig()
    d["a/b/c"] = 1

    assert len(d) == 1

    d["b/c/d"] = 2

    assert len(d) == 2

    d["b/c/e/f"] = 3

    assert len(d) == 3

    d["b/c/e/g"] = 4

    assert len(d) == 4
