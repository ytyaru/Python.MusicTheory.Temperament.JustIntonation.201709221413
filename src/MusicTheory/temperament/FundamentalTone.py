from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.OctaveClass import OctaveClass
from MusicTheory.pitch.NoteNumber import NoteNumber

class FundamentalTone:
    def __init__(self, hz=440, pitchClass=9, octaveClass=5):
#        self.__hz = hz
#        self.__pitchClass = pitchClass
#        self.__octaveClass = octaveClass
#        self.__hz = -1
#        self.__pitchClass = -1
#        self.__octaveClass = -1
#        self.__noteNumber = -1
        self.__hz = hz
        self.__pitchClass = pitchClass
        self.__octaveClass = octaveClass
        self.__noteNumber = -1
        self.Hz = hz
        self.PitchClass = pitchClass
        self.OctaveClass = octaveClass
#        self.Hz = hz
#        self.PitchClass = pitchClass
#        self.OctaveClass = octaveClass
#        self.NoteNumber = NoteNumber.Get(pitchClass, octaveClass)
#        self.__noteNumber = NoteNumber.Get(self.__pitchClass, self.__octaveClass)
    @property
    def Hz(self): return self.__hz
    @Hz.setter
    def Hz(self, v):
        if not isinstance(v, (int, float)): raise TypeError('Hzは数値型(int, float)にしてください。')
        if v < 0: raise ValueError('Hzは0以上の数値にしてください。')
        self.__hz = v
    @property
    def PitchClass(self): return self.__pitchClass
    @PitchClass.setter
    def PitchClass(self, v):
        p = PitchClass.Get(v)[0]
        self.__pitchClass = p
        self.__noteNumber = NoteNumber.Get(p, self.OctaveClass)
    @property
    def OctaveClass(self): return self.__octaveClass
    @OctaveClass.setter
    def OctaveClass(self, v):
        o = OctaveClass.Get(v, _min=0)
        self.__octaveClass = o
        self.__noteNumber = NoteNumber.Get(self.PitchClass, o)
    @property
    def NoteNumber(self): return self.__noteNumber
    @NoteNumber.setter
    def NoteNumber(self, v):
        self.__pitchClass, self.__octaveClass = PitchClass.Get(v)
        self.__noteNumber = v

