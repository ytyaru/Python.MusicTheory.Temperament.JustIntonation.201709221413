#!python3.6
import unittest
import math
from MusicTheory.temperament.EqualTemperament import EqualTemperament
from MusicTheory.temperament.FundamentalTone import FundamentalTone
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.OctaveClass import OctaveClass
from MusicTheory.pitch.NoteNumber import NoteNumber
import Framework.ConstMeta
"""
EqualTemperamentのテスト。
http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/DTM/freq_map.html
"""
class TestEqualTemperament(unittest.TestCase):
    def test_init_Default(self):
        e = EqualTemperament()
        self.assertTrue(isinstance(e.FundamentalTone, FundamentalTone))
        self.assertEqual(440, e.FundamentalTone.Hz)
        self.assertEqual(9, e.FundamentalTone.PitchClass)
        self.assertEqual(5, e.FundamentalTone.OctaveClass)
    def test_init_set(self):
        f = FundamentalTone(hz=432, pitchClass=9, octaveClass=5)
        e = EqualTemperament(f)
        self.assertTrue(isinstance(e.FundamentalTone, FundamentalTone))
        self.assertEqual(432, e.FundamentalTone.Hz)
        self.assertEqual(9, e.FundamentalTone.PitchClass)
        self.assertEqual(5, e.FundamentalTone.OctaveClass)
        del f
        with self.assertRaises(ReferenceError) as ex:            
            print(e.FundamentalTone)
        self.assertIn('weakly-referenced object no longer exists', str(ex.exception))
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


if __name__ == '__main__':
    unittest.main()

