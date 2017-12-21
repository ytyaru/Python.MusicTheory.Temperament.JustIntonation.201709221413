#!python3.6
import unittest
import math
from MusicTheory.temperament.PythagoreanTuning import PythagoreanTuning
from MusicTheory.temperament.FundamentalTone import FundamentalTone
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.OctaveClass import OctaveClass
from MusicTheory.pitch.NoteNumber import NoteNumber
import Framework.ConstMeta
"""
PythagoreanTuningのテスト。
"""
class TestPythagoreanTuning(unittest.TestCase):
    def test_init_Default(self):
        p = PythagoreanTuning()
        self.assertTrue(isinstance(p.FundamentalTone, FundamentalTone))
        self.assertEqual(440, p.FundamentalTone.Hz)
        self.assertEqual(9, p.FundamentalTone.PitchClass)
        self.assertEqual(5, p.FundamentalTone.OctaveClass)
    def test_init_set(self):
        f = FundamentalTone(hz=432, pitchClass=9, octaveClass=5)
        p = PythagoreanTuning(f)
        self.assertTrue(isinstance(p.FundamentalTone, FundamentalTone))
        self.assertEqual(432, p.FundamentalTone.Hz)
        self.assertEqual(9, p.FundamentalTone.PitchClass)
        self.assertEqual(5, p.FundamentalTone.OctaveClass)
        del f
        with self.assertRaises(ReferenceError) as ex:            
            print(p.FundamentalTone)
        self.assertIn('weakly-referenced object no longer exists', str(ex.exception))
        
    def test_Get(self):
        f = FundamentalTone(hz=440, pitchClass=9, octaveClass=5)
        p = PythagoreanTuning(f)
        for pitch in range(PitchClass.Max+1):
            hz = p.GetFrequency(pitch, 5)
            print(hz)
            if 9 == pitch: self.assertEqual(440, math.floor(hz))
            
    def test_Get_AllOctave_440(self):
        f = FundamentalTone(hz=440, pitchClass=9, octaveClass=5)
        p = PythagoreanTuning(f)
        for octave in range(10+1):
            hz = p.GetFrequency(9, octave)
            print(hz)
            self.assertEqual(math.floor(440*pow(2,octave-5)), math.floor(hz))
        # A10(9,10)はMIDIノート番号(0〜127)の範囲を超えている！
            
    def test_Get_AllOctave_432(self):
        f = FundamentalTone(hz=432, pitchClass=9, octaveClass=5)
        p = PythagoreanTuning(f)
        for octave in range(10+1):
            hz = p.GetFrequency(9, octave)
            self.assertEqual(math.floor(432*pow(2,octave-5)), math.floor(hz))

    def test_Get_Invalid_Type_PitchClass(self):
        p = PythagoreanTuning()
        with self.assertRaises(TypeError) as ex:
            p.GetFrequency('pitch', 5)
#        self.assertIn('引数pitchClass, relativeOctaveはint型にしてください。', str(ex.exception))
        self.assertIn('引数pitchClassはint型にしてください。', str(ex.exception))        
    def test_Get_Invalid_Type_OctaveClass(self):
        p = PythagoreanTuning()
        with self.assertRaises(TypeError) as ex:
            p.GetFrequency(9, 'octave')
#        self.assertIn('引数pitchClass, relativeOctaveはint型にしてください。', str(ex.exception))
        self.assertIn('引数octaveはint型にしてください。', str(ex.exception))
    def test_Get_OutOfRange_Pitch_Min(self):
        p = PythagoreanTuning()
        with self.assertRaises(ValueError) as ex:
            p.GetFrequency(-1, 5)
        self.assertIn(f'引数pitchClassは{PitchClass.Min}〜{PitchClass.Max}までの整数値にしてください。', str(ex.exception))
    def test_Get_OutOfRange_Pitch_Max(self):
        p = PythagoreanTuning()
        with self.assertRaises(ValueError) as ex:
            p.GetFrequency(12, 5)
        self.assertIn(f'引数pitchClassは{PitchClass.Min}〜{PitchClass.Max}までの整数値にしてください。', str(ex.exception))
    def test_Get_OutOfRange_Octave_Min(self):
        p = PythagoreanTuning()
        with self.assertRaises(ValueError) as ex:
            p.GetFrequency(9, -1)
#        self.assertIn('ノート番号が0〜127の範囲外になりました。', str(ex.exception))
        self.assertIn('引数octaveは0〜10の値にしてください。', str(ex.exception))
        
    def test_Get_OutOfRange_Octave_Max(self):
        p = PythagoreanTuning()
        with self.assertRaises(ValueError) as ex:
            p.GetFrequency(9, 11)
#        self.assertIn('ノート番号が0〜127の範囲外になりました。', str(ex.exception))
        self.assertIn('引数octaveは0〜10の値にしてください。', str(ex.exception))


if __name__ == '__main__':
    unittest.main()

