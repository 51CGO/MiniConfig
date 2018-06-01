#!/usr/bin/env python3

import collections
import json

VALUE_TYPES = [str, int, float, bool, None]


class MiniConfig(collections.MutableMapping):

    def __init__(self, data={}, separator="/"):

        self.separator = separator
        self.data = {}
        self.update(data)

    def __getitem__(self, path):

        list_keys = path.split(self.separator)

        dict_cur = self.data

        for key in list_keys:

            if key not in dict_cur:
                raise KeyError(path)

            dict_cur = dict_cur[key]

        return dict_cur

    def __setitem__(self, path, value):

        if type(path) != str:
            raise TypeError("path must be a string")

        if path == "":
            raise ValueError("path must not be empty")

        if type(value) not in [dict] + VALUE_TYPES:
            raise TypeError("%s is not an allowed type for value" % type(value))

        list_keys = path.split(self.separator)

        dict_cur = self.data

        for key in list_keys[:-1]:

            if key not in dict_cur:
                dict_cur[key] = {} #MiniConfig(separator=self.separator)

            dict_cur = dict_cur[key]

        dict_cur[list_keys[-1]] = value

    def __delitem__(self, path):

        list_keys = path.split(self.separator)

        dict_cur = self.data

        for key in list_keys:

            if key not in dict_cur:
                raise KeyError(path)

            dict_cur = dict_cur[key]

        del dict_cur

    def __len__(self):

        return len([k for k in self])

    def __iter__(self):

        for key in [k for k in rwalk(self.data, self.separator)]:
            yield key

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)

    def write(self,path_output):
        fp = open(path_output, "w")
        json.dump(self.data, fp, indent=2, sort_keys=True)
        fp.close()

    def read(self, path_input):
        fp = open(path_input)
        self.update(json.load(fp))
        fp.close()


def rwalk(dict_input, separator):

    for key in dict_input:

        if type(dict_input[key]) in VALUE_TYPES:
            yield key

        elif type(dict_input[key]) == dict:
            for subkey in rwalk(dict_input[key], separator):
                yield "%s%s%s" % (key, separator, subkey)
