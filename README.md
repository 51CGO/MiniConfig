### MiniConfig

MiniConfig is an easy way to manage recursive dictionaries:

    >>> import miniconfig
    >>> d = miniconfig.MiniConfig()
    >>> d["a/b/c"] = 1
    >>> d
    {'a': {'b': {'c': 1}}}
    >>> d["a/b/c"]
    1

MiniConfig is based on collections.MutableMapping.
