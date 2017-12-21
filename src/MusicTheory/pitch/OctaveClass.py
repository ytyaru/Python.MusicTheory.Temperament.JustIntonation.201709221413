#!python3.6
import collections
from Framework.ConstMeta import ConstMeta
"""
絶対値オクターブから相対オクターブ値（ゼロ基準のオクターブ値。オクターブクラス（ピッチクラスに似せた））を取得する。
"""
class OctaveClass(metaclass=ConstMeta):
    def __new__(cls):
        cls.Range = 10
    
    @classmethod
    def Get(cls, octave, _min=-1):
        cls.Validate(octave, _min)
        if _min < 0: return octave + abs(_min)
        else: return octave - abs(_min)

    @classmethod
    def Validate(cls, octave, _min):
        if not isinstance(octave, int): raise TypeError(f'引数octaveはint型にしてください。: type(octave)={type(octave)}')
        if not isinstance(_min, int): raise TypeError(f'引数_minはint型にしてください。: type(_min)={type(_min)}')
        if octave < _min or _min+cls.Range < octave: raise ValueError(f'引数octaveは{_min}〜{_min + cls.Range}の値にしてください。: octave={octave}')
