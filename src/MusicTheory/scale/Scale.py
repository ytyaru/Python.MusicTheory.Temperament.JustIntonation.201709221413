from MusicTheory.scale.ScaleIntervals import ScaleIntervals
#from MusicTheory.pitch.PitchClass import PitchClass
#from MusicTheory.pitch.OctaveClass import OctaveClass
#from Framework.ConstMeta import ConstMeta
from MusicTheory.pitch.PitchClass import PitchClass
class Scale:
    def __init__(self, key=0, intervals=ScaleIntervals.Major):
#        self.__key = -1 # PitchClass(0〜11)
#        self.__intervals = ScaleIntervals.Major
        self.__key = key
        self.__intervals = intervals
    @property
    def Key(self): return self.__key
    @Key.setter
    def Key(self, v): self.__key = PitchClass.Get(v)[0]
    @property
    def Intervals(self): return self.__intervals
    @Intervals.setter
    def Intervals(self, v):
        if not isinstance(v, (tuple, list)): raise TypeError('引数intervalsはtuple, listのいずれかにしてください。: type(v)={type(v)}')
        for i in v:
            if not isinstance(i, int): raise TypeError('引数intervalsの要素はint型にしてください。: type(i)={type(i)}')
            if i <= 0: raise ValueError('引数intervalsの要素は0より大きい整数値にしてください。: i={i}, v={v}')
#            PitchClass.Validate(i)
#        for i in v: PitchClass.Validate(i)
        self.__intervals = v
