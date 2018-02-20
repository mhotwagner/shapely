from collections import defaultdict


class dynamicdefaultdict(defaultdict):
    """
    Slightly modified defaultdict that
    passes the key into the default_factory function
    """
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret
