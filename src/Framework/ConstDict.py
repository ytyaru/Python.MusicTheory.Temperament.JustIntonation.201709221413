#https://stackoverflow.com/questions/2703599/what-would-a-frozen-dict-be
#https://docs.python.jp/3/library/collections.html#userdict-objects
import collections
class ConstDict(dict):
    class ConstError(TypeError): pass
    def __setitem__(self, name, value):
        if name in self.keys(): raise self.ConstError('readonly。再代入禁止です。')
        self[name] = value

"""
if __name__ == '__main__':
    cd = ConstDict({'k': 'v'})
    print(dir(cd))
    print(cd)
    print(cd['k'])
    cd['k'] = 'v2'#TypeError: 'FrozenDict' object does not support item assignment
    print(cd['k'])
"""
