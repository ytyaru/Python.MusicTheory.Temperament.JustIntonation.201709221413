import collections
class ConstOrderedDict(collections.OrderedDict):
    class ConstError(TypeError): pass
    def __setitem__(self, name, value):
        if name in self.keys(): raise self.ConstError('readonly。再代入禁止です。')
        collections.OrderedDict.__setitem__(self, name, value)
#        super()[name] = value#TypeError: 'super' object does not support item assignment
#        super(collections.OrderedDict, self)[name] = value#TypeError: 'super' object does not support item assignment

"""
if __name__ == '__main__':
    cd = ConstOrderedDict((('k','v'),('a','b')))
    print(dir(cd))
    print(cd)
    print(cd['k'])
    cd['k'] = 'v2'#TypeError: 'FrozenDict' object does not support item assignment
    print(cd['k'])
"""
