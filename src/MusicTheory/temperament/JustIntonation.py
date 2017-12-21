import weakref
import math
from MusicTheory.temperament.FundamentalTone import FundamentalTone
from MusicTheory.scale.Scale import Scale
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.OctaveClass import OctaveClass
from Framework.ConstMeta import ConstMeta
"""
※音階の構成音を固定比で算出するものである。P1,M3,P5の長三和音は綺麗だが、M2,P4,M6の短三和音は汚い。

純正律で周波数を取得する。
純正律は同一音名でも調が変わると周波数も変わる。
1. 基音を定める
2. 基音から12音の周波数を算出する
3. 調から構成音を含めた12音を算出する

12音の算出は和音の組合せによって変わる、かもしれない。よくわからないが、今回は固定比で算出してしまう。
http://musica.art.coocan.jp/enharmonic.htm
http://yppts.adam.ne.jp/music/comp.html
"""
class JustIntonation(metaclass=ConstMeta):
    # C,C#,D,D#,E,F,F#,G,G#,A,A#,B
    __Rate = [1,17/16,9/8,6/5,5/4,4/3,17/12,3/2,8/5,5/3,30/17,15/8]

    def __init__(self, fundamentalTone=None, scale=None):
        if None is fundamentalTone: self.__fundamentalTone = FundamentalTone()
        else:
            if not isinstance(fundamentalTone, FundamentalTone): raise TypeError('引数fundamentalToneはFundamentalTone型にしてください。: type(fundamentalTone)={type(fundamentalTone)}')
            self.__fundamentalTone = weakref.proxy(fundamentalTone)
        if None is scale: self.__scale = Scale()
        else:
            if not isinstance(scale, Scale): raise TypeError('引数scaleはScale型にしてください。: type(scale)={type(scale)')
            self.__scale = weakref.proxy(scale)
        self.__Frequencies = []
        self.__ScaleFrequencies = []
#        self.__calcFrequencies()
#        self.__calcScaleFrequencies()
        self.__calcFrequencies(self.__Frequencies, self.FundamentalTone.Hz)
        self.__flatOctave(self.__Frequencies, self.FundamentalTone.PitchClass)
        self.__calcFrequencies(self.__ScaleFrequencies, self.__Frequencies[self.Scale.Key])
#        self.__flatOctave(self.__ScaleFrequencies, self.Scale.Key)
    
    @property
    def FundamentalTone(self): return self.__fundamentalTone
    @property
    def Scale(self): return self.__scale
    
    # 純正律は同一音名でも調や音階が変わると周波数も変わる。
    def GetFrequency(self, pitchClass, octaveClass):
        PitchClass.Validate(pitchClass)
        OctaveClass.Validate(octaveClass, _min=0)
        return self.__ScaleFrequencies[pitchClass] * math.pow(2, octaveClass - self.FundamentalTone.OctaveClass)

    def __calcFrequencies(self, targetList, BaseHz):
        targetList.clear()
        for rate in self.__Rate: targetList.append(rate * BaseHz)
        #C音から始まるようにする
#        self.__flatOctave()

    def __flatOctave(self, targetList, startPitchClass):
        #オクターブ合わせ 基音(A=440Hz)としたとき、C以降は次のオクターブの音である。12-9=3, 3音目までは同一オクターブ内。それ以降は1オクターブさげる(1/2にする)
        if 0 == startPitchClass: return
        sameClass = (PitchClass.Max+1) - startPitchClass
        for i in range(sameClass, len(targetList)):
            targetList[i] /= 2
        #低音(C音)から始まるようにする
        targetList.sort()

