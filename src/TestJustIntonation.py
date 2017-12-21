#!python3.6
import unittest
import math
from MusicTheory.temperament.JustIntonation import JustIntonation
from MusicTheory.temperament.FundamentalTone import FundamentalTone
from MusicTheory.scale.Scale import Scale
from MusicTheory.scale.ScaleIntervals import ScaleIntervals
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.OctaveClass import OctaveClass
from MusicTheory.pitch.NoteNumber import NoteNumber
import Framework.ConstMeta
"""
JustIntonationのテスト。
"""
class TestJustIntonation(unittest.TestCase):
    def test_init_Default(self):
        j = JustIntonation()
        self.assertTrue(isinstance(j.FundamentalTone, FundamentalTone))
        self.assertEqual(440, j.FundamentalTone.Hz)
        self.assertEqual(9, j.FundamentalTone.PitchClass)
        self.assertEqual(5, j.FundamentalTone.OctaveClass)
        self.assertTrue(isinstance(j.Scale, Scale))
        self.assertTrue(j.Scale.Key == 0)
        self.assertTrue(j.Scale.Intervals == ScaleIntervals.Major)
    def test_init_None(self):
        j = JustIntonation(None,None)
        self.assertTrue(isinstance(j.FundamentalTone, FundamentalTone))
        self.assertEqual(440, j.FundamentalTone.Hz)
        self.assertEqual(9, j.FundamentalTone.PitchClass)
        self.assertEqual(5, j.FundamentalTone.OctaveClass)
        self.assertTrue(isinstance(j.Scale, Scale))
        self.assertTrue(j.Scale.Key == 0)
        self.assertTrue(j.Scale.Intervals == ScaleIntervals.Major)
    def test_init_set(self):
        f = FundamentalTone(hz=432, pitchClass=9, octaveClass=5)
        s = Scale(0, ScaleIntervals.Minor)
        j = JustIntonation(f, s)
        self.assertTrue(isinstance(j.FundamentalTone, FundamentalTone))
        self.assertEqual(432, j.FundamentalTone.Hz)
        self.assertEqual(9, j.FundamentalTone.PitchClass)
        self.assertEqual(5, j.FundamentalTone.OctaveClass)
        self.assertTrue(isinstance(j.Scale, Scale))
        self.assertTrue(j.Scale.Key == 0)
        self.assertTrue(j.Scale.Intervals == ScaleIntervals.Minor)
        del f
        with self.assertRaises(ReferenceError) as ex:            
            print(j.FundamentalTone)
        self.assertIn('weakly-referenced object no longer exists', str(ex.exception))
        del s
        with self.assertRaises(ReferenceError) as ex:            
            print(j.Scale)
        self.assertIn('weakly-referenced object no longer exists', str(ex.exception))
    def test_init_Invalid_Type_FundamentalTone(self):
        with self.assertRaises(TypeError) as ex:
            j = JustIntonation('')
        self.assertIn('引数fundamentalToneはFundamentalTone型にしてください。', str(ex.exception))
    def test_init_Scale_Type_FundamentalTone(self):
        with self.assertRaises(TypeError) as ex:
            j = JustIntonation(None, '')
        self.assertIn('引数scaleはScale型にしてください。', str(ex.exception))
    def test_Get_A4(self):
        print('基音=A4(440Hz) 調=A4')
        f = FundamentalTone(hz=440, pitchClass=9, octaveClass=5)
        s = Scale(9, ScaleIntervals.Major)
        j = JustIntonation(f, s)
        for p in range(PitchClass.Max+1):
            print(j.GetFrequency(p, 5))
            #正解の基準がない。出た数値が正解ということにする。
    def test_Get_C4(self):
        print('基音=A4(440Hz) 調=C4')
        f = FundamentalTone(hz=440, pitchClass=9, octaveClass=5)
        s = Scale(0, ScaleIntervals.Major)
        j = JustIntonation(f, s)
        for p in range(PitchClass.Max+1):
            print(j.GetFrequency(p, 5))
            #正解の基準がない。出た数値が正解ということにする。
        print('純正律の周波数において、正解の基準が見つけられなかった。出た数値が正解ということにする。')
    
    """
    def test_Get(self):
        print('test_Get')
        e = EqualTemperament()
        expecteds = [261,277,293,311,329,349,369,391,415,440,466,493]
        for p in range(PitchClass.Max+1):
            print(e.GetFrequency(p, 5))
            self.assertEqual(expecteds[p], math.floor(e.GetFrequency(p, 5)))
    def test_Get_MinOctave(self):
        print('test_Get_MinOctave')
        e = EqualTemperament()
        expecteds = [261,277,293,311,329,349,369,391,415,440,466,493]
        for p in range(PitchClass.Max+1):
            print(e.GetFrequency(p, 0))
            self.assertEqual(math.floor(expecteds[p]/math.pow(2,5)), math.floor(e.GetFrequency(p, 0)))
    def test_Get_MaxOctave(self):
        print('test_Get_MaxOctave')
        e = EqualTemperament()
        expecteds = [8372,8869,9397,9956,10548,11175,11839,12543]
        for p in range(PitchClass.Max+1):
            if p + (10 * (PitchClass.Max+1)) < 128:
                print(e.GetFrequency(p, 10))
                self.assertEqual(expecteds[p], math.floor(e.GetFrequency(p, 10)))
    def test_Get_Low(self):
        print('test_Get_Low')
        e = EqualTemperament()
        expecteds = [261,277,293,311,329,349,369,391,415,440,466,493]
        for p in range(PitchClass.Max+1):
            print(e.GetFrequency(p, 5-1))
            self.assertEqual(math.floor(expecteds[p]/2), math.floor(e.GetFrequency(p, 5-1)))
    def test_Get_Hi(self):
        print('test_Get_Low')
        e = EqualTemperament()
        expecteds = [261,277,293,311,329,349,369,391,415,440,466,493]
        for p in range(PitchClass.Max+1):
            print(e.GetFrequency(p, 5+1))
            self.assertIn(math.floor(e.GetFrequency(p, 5+1)), [math.floor(expecteds[p]*2), math.floor(expecteds[p]*2)+1])

    def test_Get_Invalid_Type_PitchClass(self):
        e = EqualTemperament()
        with self.assertRaises(TypeError) as ex:
            e.GetFrequency('pitch', 5)
        self.assertIn('引数pitchClassはint型にしてください。', str(ex.exception))
    def test_Get_Invalid_Type_OctaveClass(self):
        e = EqualTemperament()
        with self.assertRaises(TypeError) as ex:
            e.GetFrequency(9, 'octave')
        self.assertIn('引数octaveはint型にしてください。', str(ex.exception))
    def test_Get_OutOfRange_Pitch_Min(self):
        e = EqualTemperament()
        with self.assertRaises(ValueError) as ex:
            e.GetFrequency(-1, 5)
        self.assertIn(f'引数pitchClassは{PitchClass.Min}〜{PitchClass.Max}までの整数値にしてください。', str(ex.exception))
    def test_Get_OutOfRange_Pitch_Max(self):
        e = EqualTemperament()
        with self.assertRaises(ValueError) as ex:
            e.GetFrequency(12, 5)
        self.assertIn(f'引数pitchClassは{PitchClass.Min}〜{PitchClass.Max}までの整数値にしてください。', str(ex.exception))
    def test_Get_OutOfRange_Octave_Min(self):
        e = EqualTemperament()
        with self.assertRaises(ValueError) as ex:
            e.GetFrequency(9, -1)
        self.assertIn('引数octaveは0〜10の値にしてください。', str(ex.exception))
    def test_Get_OutOfRange_Octave_Max(self):
        e = EqualTemperament()
        with self.assertRaises(ValueError) as ex:
            e.GetFrequency(9, 11)
        self.assertIn('引数octaveは0〜10の値にしてください。', str(ex.exception))
    """


if __name__ == '__main__':
    unittest.main()

