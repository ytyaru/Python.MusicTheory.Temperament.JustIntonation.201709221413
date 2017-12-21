#https://stackoverflow.com/questions/2703599/what-would-a-frozen-dict-be
"""
from Framework.ConstMeta import ConstMeta
import collections
class ConstDict(collections.UserDict, metaclass=ConstMeta): pass
"""
import collections
class FrozenDict(collections.Mapping):
    def __init__(self, *args, **kwargs):
        self._d = dict(*args, **kwargs)
        self._hash = None
    def __iter__(self): return iter(self._d)
    def __len__(self): return len(self._d)
    def __getitem__(self, key): return self._d[key]
    def __hash__(self):
        if self._hash is None:
            self._hash = 0
            for pair in self.iteritems():
                self._hash ^= hash(pair)
        return self._hash

if __name__ == '__main__':
    fd = FrozenDict({'k': 'v'})
    print(fd)
    print(fd['k'])
    fd['k'] = 'v2'#TypeError: 'FrozenDict' object does not support item assignment
    print(fd['k'])
