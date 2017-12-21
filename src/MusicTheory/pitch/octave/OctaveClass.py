#!python3.6
import collections
from Framework.ConstMeta import ConstMeta
"""
絶対値オクターブから相対オクターブ値（ゼロ基準のオクターブ値。オクターブクラス（ピッチクラスに似せた））を取得する。
"""
class OctaveClass(metaclass=ConstMeta):
    @classmethod
    def Get(cls, halfToneNum:int):
        if not isinstance(halfToneNum, int): raise TypeError(f'引数halfToneNumはint型にしてください。: type(halfToneNum)={type(halfToneNum)}')
        pitchClass = halfToneNum % (cls.Max+1)
        relativeOctave = halfToneNum // (cls.Max+1)
        if pitchClass < cls.Min:
            pitchClass += (cls.Max+1)
        return cls.__PitchClass(pitchClass, relativeOctave)

    @classmethod
    def Validate(cls, pitchClass:int):
        if not isinstance(pitchClass, int): raise TypeError(f'引数pitchClassはint型にしてください。: type(pitchClass)={type(pitchClass)}')
        if pitchClass < cls.Min or cls.Max < pitchClass: raise ValueError(f'引数pitchClassは{cls.Min}〜{cls.Max}までの整数値にしてください。')

