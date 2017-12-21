#!python3.6
import unittest
from MusicTheory.pitch.OctaveClass import OctaveClass
#from MusicTheory.pitch.octave.SPN import SPN
#from MusicTheory.pitch.octave.YAMAHA import YAMAHA
#from MusicTheory.pitch.octave.ZERO import ZERO
import Framework.ConstMeta
"""
PitchClassのテスト。
"""
class TestOctaveClass(unittest.TestCase):
    def test_Range(self):
        self.assertEqual(10, OctaveClass.Range)
    def test_SPN_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            OctaveClass.Range = 'some value.'
        self.assertEqual(str(e.exception), 'readonly。再代入禁止です。')
    def test_Get(self):
        for o in range(-1, 9+1):
            self.assertEqual((o+1), OctaveClass.Get(o))
    def test_Get_SPN(self):
        for o in range(-1, 9+1):
            self.assertEqual((o+1), OctaveClass.Get(o, _min=-1))    
    def test_Get_YAMAHA(self):
        for o in range(-2, 8+1):
            self.assertEqual((o+2), OctaveClass.Get(o, _min=-2))
    def test_Get_ZERO(self):
        for o in range(0, 10+1):
            self.assertEqual((o+0), OctaveClass.Get(o, _min=0))
    def test_Get_Invalid_Type(self):
        with self.assertRaises(TypeError) as e: #TypeError: not all arguments converted during string formatting
            OctaveClass.Get('無効な型')
        self.assertIn('引数octaveはint型にしてください。', str(e.exception))        
        with self.assertRaises(TypeError) as e: #TypeError: not all arguments converted during string formatting
            OctaveClass.Get(0, _min='abc')
        self.assertIn('引数_minはint型にしてください。', str(e.exception))        

    def test_Get_SPN_OutOfRange(self):
        _min = 0
        with self.assertRaises(ValueError) as e:
            OctaveClass.Get(-1, _min)
        self.assertIn(f'引数octaveは{_min}〜{_min + OctaveClass.Range}の値にしてください。', str(e.exception))        
        with self.assertRaises(ValueError) as e:
            OctaveClass.Get(11, _min)
        self.assertIn(f'引数octaveは{_min}〜{_min + OctaveClass.Range}の値にしてください。', str(e.exception))        
        _min = -1
        with self.assertRaises(ValueError) as e:
            OctaveClass.Get(-2, _min)
        self.assertIn(f'引数octaveは{_min}〜{_min + OctaveClass.Range}の値にしてください。', str(e.exception))        
        with self.assertRaises(ValueError) as e:
            OctaveClass.Get(10, _min)
        self.assertIn(f'引数octaveは{_min}〜{_min + OctaveClass.Range}の値にしてください。', str(e.exception))        
        _min = -2
        with self.assertRaises(ValueError) as e:
            OctaveClass.Get(-3, _min)
        self.assertIn(f'引数octaveは{_min}〜{_min + OctaveClass.Range}の値にしてください。', str(e.exception))        
        with self.assertRaises(ValueError) as e:
            OctaveClass.Get(9, _min)
        self.assertIn(f'引数octaveは{_min}〜{_min + OctaveClass.Range}の値にしてください。', str(e.exception))        
        
            
if __name__ == '__main__':
    unittest.main()

