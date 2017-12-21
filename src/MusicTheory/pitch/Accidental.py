#!python3.6
from Framework.ConstMeta import ConstMeta
"""
変化記号から相対半音数を取得する。
"""
class Accidental(metaclass=ConstMeta):
    def __new__(cls):
        cls.Accidentals = {'♯': 1, '#': 1, '+': 1, '♭': -1, 'b': -1, '-': -1}
        cls.Languages = ['en','ja','de','it','fr','es','zh']
        cls.__SharpNames = dict(zip(cls.Languages, ['sharp','嬰','is','diesis','dièse', 'sostenido','升']))
        cls.__FlatNames = dict(zip(cls.Languages, ['flat','変','es','bemolle','bémol','bemol','降']))
        cls.__DoubleNames = dict(zip(cls.Languages, ['double','重','*2','doppio','double','doble','重']))
    
    @classmethod
    def Get(cls, accidental:str):
        if not cls.__CheckParameter(accidental): return 0
        return sum([cls.Accidentals[c] for c in accidental])

    @classmethod
    def __CheckParameter(cls, accidental):
        if None is accidental: return False
        if not isinstance(accidental, str): raise TypeError(f'引数accidentalは文字列型にしてください。: {cls.Accidentals.keys()}')
        if 0 == len(accidental): return False
        cls.__IsSameChars(accidental)
        if accidental[0] not in cls.Accidentals.keys(): raise ValueError(f'引数accidentalに使える文字は次のものだけです。: {cls.Accidentals.keys()}')
        return True

    @classmethod
    def __IsSameChars(cls, accidental):
        for c in accidental:
            if c != accidental[0]: raise ValueError(f'引数accidentalは同じ文字のみ連続使用を許されます。異なる文字を混在させることはできません。: {accidental}')
        return True

    @classmethod
    def GetName(cls, accidental:str, lang='ja'):
        # 1  : Sharp
        # 2  : Double Sharp
        # 3〜: Sharp*3
        if not cls.__CheckParameter(accidental): return ''
        if lang not in cls.Languages: raise ValueError(f'引数langは次のうちのいずれかにしてください。{cls.Languages}: lang={lang}')
        isSharp = True if 0 < cls.Accidentals[accidental[0]] else False
        count = len(accidental)
        if 1 == count: return cls.__SharpNames[lang] if isSharp else cls.__FlatNames[lang]
        elif 2 == count:
            name = cls.__SharpNames[lang] if isSharp else cls.__FlatNames[lang]
            if 'de' == lang: return name * 2
            elif 'es' == lang: return name + ' ' + cls.__DoubleNames[lang]
            elif 'ja' == lang or 'zh' == lang: return cls.__DoubleNames[lang] + name
            else: return cls.__DoubleNames[lang] + ' ' + name
        else:
            name = cls.__SharpNames[lang] if isSharp else cls.__FlatNames[lang]
            return name + '*' + str(count)

