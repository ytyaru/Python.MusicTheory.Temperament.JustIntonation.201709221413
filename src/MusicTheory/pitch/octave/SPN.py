#!python3.6
import collections
from Framework.ConstMeta import ConstMeta
from MusicTheory.pitch.octave.OctaveClass import OctaveClass
    
class SPN(metaclass=OctaveClass):
    def __new__(cls):
        cls.Min = -1
        cls.Names = {'ja': '国際式'}
        cls.Descriptions = {'ja': '88鍵盤の最低音がA0になる。'}

#    Min = -1
#    Names = {'ja': '国際式'}
#    Descriptions = {'ja': '88鍵盤の最低音がA0になる。'}

class_datas = (
{'name':'SPN', 'members': {'Min':-1, 'Names':{'ja': '国際式'}, 'Descriptions':{'ja': '88鍵盤の最低音がA0になる。'}}},
{'name':'YAMAHA', 'members': {'Min':-2, 'Names':{'ja': 'YAMAHA式'}, 'Descriptions':{'ja': '根拠不明。'}}},
{'name':'ZERO', 'members': {'Min':0, 'Names':{'ja': 'ゼロ式'}, 'Descriptions':{'ja': 'OctaveClassと同値。最低周波数のオクターブを0とする。'}}}
)

OctaveTypes = []
for cd in class_datas:
    Type = type(cd['name'], (OctaveClass,), cd['members'])
    OctaveTypes.append(Type)

print(OctaveTypes)
for t in OctaveTypes:
#    print(isinstance(t, OctaveClass))
    print(issubclass(t, OctaveClass))
    print(t.Min)
    print(t.Names)
    print(t.Descriptions)
OctaveTypes[0].Min = 100

