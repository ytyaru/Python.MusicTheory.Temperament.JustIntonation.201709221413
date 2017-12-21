#!python3.6
import unittest
from MusicTheory.temperament.FundamentalTone import FundamentalTone
from MusicTheory.pitch.NoteNumber import NoteNumber
import Framework.ConstMeta
"""
FundamentalToneのテスト。
"""
class TestFundamentalTone(unittest.TestCase):
    def test_Default(self):
        f = FundamentalTone()
        self.assertEqual(440, f.Hz)
        self.assertEqual(9, f.PitchClass)
        self.assertEqual(5, f.OctaveClass)
        self.assertEqual(NoteNumber.Get(9,5), f.NoteNumber)
    def test_init(self):
        f = FundamentalTone(hz=261, pitchClass=0, octaveClass=5)
        self.assertEqual(261, f.Hz)
        self.assertEqual(0, f.PitchClass)
        self.assertEqual(5, f.OctaveClass)
        self.assertEqual(NoteNumber.Get(0,5), f.NoteNumber)
    def test_init_OutOfRange_Hz(self):
        with self.assertRaises(ValueError) as e:
            f = FundamentalTone(hz=-1, pitchClass=0, octaveClass=5)
        self.assertIn('Hzは0以上の数値にしてください。', str(e.exception))        
    def test_init_PitchClass(self):
        f = FundamentalTone(hz=0, pitchClass=-1, octaveClass=5)
        self.assertEqual(11, f.PitchClass)
        self.assertEqual(5, f.OctaveClass)
    def test_init_PitchClass(self):
        f = FundamentalTone(hz=0, pitchClass=12, octaveClass=5)
        self.assertEqual(0, f.PitchClass)
        self.assertEqual(5, f.OctaveClass)
    def test_init_OutOfRange_OctaveClass(self):
        with self.assertRaises(ValueError) as e:
            f = FundamentalTone(hz=440, pitchClass=0, octaveClass=-1)
        self.assertIn('ノート番号が0〜127の範囲外になりました。', str(e.exception))
    def test_set_Hz(self):
        f = FundamentalTone(hz=440, pitchClass=9, octaveClass=5)
        self.assertEqual(440, f.Hz)
        f.Hz = 555
        self.assertEqual(555, f.Hz)
    def test_set_PitchClass(self):
        f = FundamentalTone(hz=440, pitchClass=9, octaveClass=5)
        self.assertEqual(9, f.PitchClass)
        self.assertEqual(69, f.NoteNumber)
        f.PitchClass = 0
        self.assertEqual(0, f.PitchClass)
        self.assertEqual(60, f.NoteNumber)
    def test_set_OctaveClass(self):
        f = FundamentalTone(hz=440, pitchClass=9, octaveClass=5)
        self.assertEqual(5, f.OctaveClass)
        self.assertEqual(69, f.NoteNumber)
        f.OctaveClass = 4
        self.assertEqual(4, f.OctaveClass)
        self.assertEqual(57, f.NoteNumber)
    def test_set_NoteNumber(self):
        f = FundamentalTone(hz=440, pitchClass=9, octaveClass=5)
        self.assertEqual(9, f.PitchClass)
        self.assertEqual(5, f.OctaveClass)
        self.assertEqual(69, f.NoteNumber)
        f.NoteNumber = 56
        self.assertEqual(8, f.PitchClass)
        self.assertEqual(4, f.OctaveClass)
        self.assertEqual(56, f.NoteNumber)
    def test_set_Hz_Invalid_Type(self):
        with self.assertRaises(TypeError) as e:
            f = FundamentalTone(hz='hz', pitchClass=9, octaveClass=5)
        self.assertIn('Hzは数値型(int, float)にしてください。', str(e.exception))
    def test_set_PitchClass_Invalid_Type(self):
        with self.assertRaises(TypeError) as e:
            f = FundamentalTone(hz=440, pitchClass='p', octaveClass=5)
        self.assertIn('引数halfToneNumはint型にしてください。', str(e.exception))
    def test_set_OctaveClass_Invalid_Type(self):
        with self.assertRaises(TypeError) as e:
            f = FundamentalTone(hz=440, pitchClass=9, octaveClass='o')
        self.assertIn('引数pitchClass, relativeOctaveはint型にしてください。', str(e.exception))
    def test_set_NoteNumber_Invalid_Type(self):
        with self.assertRaises(TypeError) as e:
            f = FundamentalTone(hz=440, pitchClass=9, octaveClass=5)
            f.NoteNumber = 'n'
        self.assertIn('引数halfToneNumはint型にしてください。', str(e.exception))


if __name__ == '__main__':
    unittest.main()

