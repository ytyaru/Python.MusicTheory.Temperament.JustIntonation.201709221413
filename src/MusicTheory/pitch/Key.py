#!python3.6
import re
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Accidental import Accidental
from Framework.ConstMeta import ConstMeta
from Framework.ConstDict import ConstDict
"""
音名から半音数を取得する。
"""
class Key(metaclass=ConstMeta):
    def __new__(cls):
        cls.Keys = tuple('CDEFGAB')
        cls.PitchClasses = (0,2,4,5,7,9,11)
        cls.KeyNames = ConstDict({
            'en':tuple('CDEFGAB'),
            'ja':tuple('ハニホヘトイロ'), 
            'de':tuple('CDEFGAH'), 
            'it':tuple('Do,Re,Mi,Fa,Sol,La,Si'.split(',')), 
            'fr':tuple('Ut,Ré,Mi,Fa,Sol,La,Si'.split(',')),
            'es':tuple('Do,Re,Mi,Fa,Sol,La,Si'.split(',')),
            'zh':tuple('CDEFGAB'), 
        })
    
    @classmethod
    def Get(cls, name:str):
        if not (isinstance(name, str)): raise TypeError('引数nameはstr型にしてください。')
        k, a = cls.__Split(name)
        key = cls.__GetKeyHalfToneNum(k)
        accidental = Accidental.Get(a)
        return key + accidental
        
    @classmethod
    def __Split(cls, name): return (name[0], name[1:])
    
    @classmethod
    def __GetKeyHalfToneNum(cls, key:str):
        if key not in cls.Keys: raise ValueError(f'keyは次のうちのいずれかにしてください。{cls.Keys}。: key={key}')
        for i,k in enumerate(cls.Keys):
            if k == key: return cls.PitchClasses[i]

    @classmethod
    def GetName(cls, name, lang):
        if not (isinstance(name, str)): raise TypeError('引数nameはstr型にしてください。')
        if not (isinstance(lang, str)): raise TypeError('引数langはstr型にしてください。')
        if lang not in cls.KeyNames.keys(): raise ValueError(f'langは次のうちのいずれかにしてください。{cls.KeyNames.keys()}。: lang={lang}')
        k, a = cls.__Split(name)
        if k not in cls.Keys: raise ValueError(f'keyは次のうちのいずれかにしてください。{cls.Keys}。: key={k}')
        key = cls.__GetNameLangs(k, lang)
        accidental = Accidental.GetName(a, lang)
        if 'ja' == lang or 'zh' == lang: return accidental + key
        else:
            if 0 == len(accidental): return key
            else: return key + ' ' + accidental

    @classmethod
    def __GetNameLangs(cls, name, lang):
        for i,k in enumerate(cls.Keys):
            if k == name: return cls.KeyNames[lang][i]

