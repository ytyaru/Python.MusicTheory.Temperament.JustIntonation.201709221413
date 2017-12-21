import weakref
import math
from MusicTheory.temperament.FundamentalTone import FundamentalTone
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.OctaveClass import OctaveClass
class PythagoreanTuning:
    def __init__(self, fundamentalTone=None):
        if None is fundamentalTone:
            self.__fundamentalTone = FundamentalTone()
        else:
            self.__fundamentalTone = weakref.proxy(fundamentalTone)
        self.__Frequencies = []
        self.__calcFrequencies()
    
    @property
    def FundamentalTone(self): return self.__fundamentalTone

    def GetFrequency(self, pitchClass, octaveClass):
        PitchClass.Validate(pitchClass)
        OctaveClass.Validate(octaveClass, _min=0)
        return self.__Frequencies[pitchClass] * math.pow(2, octaveClass - self.FundamentalTone.OctaveClass)
        
    def __calcFrequencies(self):
        if isinstance(self.__Frequencies, (list, tuple)):
            self.__Frequencies.clear()
            self.__Frequencies.extend([f for f in self.__calcMinusInOctave()])
            self.__Frequencies.extend([f for f in self.__calcPlusInOctave()])
            self.__Frequencies.sort()
            self.__flatOctave()
    
    # return: [4, 短7, 短3, 短6, 短2] 減5は増4と同じはずだがピタゴラス音律においては別の音になってしまう（ピタゴラスコンマ）ので省く
    def __calcMinusInOctave(self):
        for x, y in ((1,1), (2,2), (3,2), (4,3), (5,3)):
            yield (((2/3)**x) * (2**y)) * self.FundamentalTone.Hz
    
    # return: [1, 5, 長2, 長6, 長3, 長7, 増4]
    def __calcPlusInOctave(self):
        yield self.FundamentalTone.Hz #1度
        yield 3/2 * self.FundamentalTone.Hz #5度
        for x, y in ((2,1), (3,1), (4,2), (5,2), (6,3)):
            yield (((3/2)**x) * (1/2**y)) * self.FundamentalTone.Hz

    # 同一オクターブにする
    def __flatOctave(self):
        #オクターブ合わせ 基音(A=440Hz)としたとき、C以降は次のオクターブの音である。12-9=3, 3音目までは同一オクターブ内。それ以降は1オクターブさげる(1/2にする)
        sameClass = (PitchClass.Max+1) - self.FundamentalTone.PitchClass
        for i in range(sameClass, len(self.__Frequencies)):
            self.__Frequencies[i] /= 2
        #低音(C音)から始まるようにする
        self.__Frequencies.sort()

