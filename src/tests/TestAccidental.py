#!python3.6
import unittest
from MusicTheory.pitch.Accidental import Accidental
import Framework.ConstMeta
"""
Accidentalのテスト。
"""
class TestAccidental(unittest.TestCase):
    def test_Accidentals(self):
        self.assertEqual(Accidental.Accidentals, {'♯': 1, '#': 1, '+': 1, '♭': -1, 'b': -1, '-': -1})
    def test_Accidentals_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            Accidental.Accidentals = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))
    def test_Get(self):
        for count in range(1, 4):
            for name, interval in Accidental.Accidentals.items():
                if not name: continue
                with self.subTest(accidenta=name, count=count):
                    self.assertEqual(Accidental.Get(name * count), interval * count)
    def test_Get_None(self): self.assertEqual(Accidental.Get(None), 0)
    def test_Get_Blank(self): self.assertEqual(Accidental.Get(''), 0)
    def test_Get_int(self):
        with self.assertRaises(TypeError) as e:
            Accidental.Get(100)
        self.assertIn('引数accidentalは文字列型にしてください。', str(e.exception))
    def test_Get_NotSameChars(self):
        with self.assertRaises(ValueError) as e:
            Accidental.Get('無効な文字')
        self.assertIn('引数accidentalは同じ文字のみ連続使用を許されます。異なる文字を混在させることはできません。', str(e.exception))
    def test_Get_Invalid(self):
        with self.assertRaises(ValueError) as e:
            Accidental.Get('無無無')
        self.assertIn('引数accidentalに使える文字は次のものだけです。', str(e.exception))
    def test_Get_Valid_NotSameChars(self):
        with self.assertRaises(ValueError) as e:
            Accidental.Get('+-')
        self.assertIn('引数accidentalは同じ文字のみ連続使用を許されます。異なる文字を混在させることはできません。', str(e.exception))

    def test_GetName_en(self):
        self.assertEqual('sharp', Accidental.GetName('#', 'en'))
        self.assertEqual('double sharp', Accidental.GetName('##', 'en'))
        self.assertEqual('sharp*3', Accidental.GetName('###', 'en'))
        self.assertEqual('flat', Accidental.GetName('b', 'en'))
        self.assertEqual('double flat', Accidental.GetName('bb', 'en'))
        self.assertEqual('flat*3', Accidental.GetName('bbb', 'en'))
        
    def test_GetName_ja(self):
        self.assertEqual('嬰', Accidental.GetName('#', 'ja'))
        self.assertEqual('重嬰', Accidental.GetName('##', 'ja'))
        self.assertEqual('嬰*3', Accidental.GetName('###', 'ja'))
        self.assertEqual('変', Accidental.GetName('b', 'ja'))
        self.assertEqual('重変', Accidental.GetName('bb', 'ja'))
        self.assertEqual('変*3', Accidental.GetName('bbb', 'ja'))
        
    def test_GetName_de(self):
        self.assertEqual('is', Accidental.GetName('#', 'de'))
        self.assertEqual('isis', Accidental.GetName('##', 'de'))
        self.assertEqual('is*3', Accidental.GetName('###', 'de'))
        self.assertEqual('es', Accidental.GetName('b', 'de'))
        self.assertEqual('eses', Accidental.GetName('bb', 'de'))
        self.assertEqual('es*3', Accidental.GetName('bbb', 'de'))
        
    def test_GetName_it(self):
        self.assertEqual('diesis', Accidental.GetName('#', 'it'))
        self.assertEqual('doppio diesis', Accidental.GetName('##', 'it'))
        self.assertEqual('diesis*3', Accidental.GetName('###', 'it'))
        self.assertEqual('bemolle', Accidental.GetName('b', 'it'))
        self.assertEqual('doppio bemolle', Accidental.GetName('bb', 'it'))
        self.assertEqual('bemolle*3', Accidental.GetName('bbb', 'it'))

    def test_GetName_fr(self):
        self.assertEqual('dièse', Accidental.GetName('#', 'fr'))
        self.assertEqual('double dièse', Accidental.GetName('##', 'fr'))
        self.assertEqual('dièse*3', Accidental.GetName('###', 'fr'))
        self.assertEqual('bémol', Accidental.GetName('b', 'fr'))
        self.assertEqual('double bémol', Accidental.GetName('bb', 'fr'))
        self.assertEqual('bémol*3', Accidental.GetName('bbb', 'fr'))
        
    def test_GetName_es(self):
        self.assertEqual('sostenido', Accidental.GetName('#', 'es'))
        self.assertEqual('sostenido doble', Accidental.GetName('##', 'es'))
        self.assertEqual('sostenido*3', Accidental.GetName('###', 'es'))
        self.assertEqual('bemol', Accidental.GetName('b', 'es'))
        self.assertEqual('bemol doble', Accidental.GetName('bb', 'es'))
        self.assertEqual('bemol*3', Accidental.GetName('bbb', 'es'))

    def test_GetName_zh(self):
        self.assertEqual('升', Accidental.GetName('#', 'zh'))
        self.assertEqual('重升', Accidental.GetName('##', 'zh'))
        self.assertEqual('升*3', Accidental.GetName('###', 'zh'))
        self.assertEqual('降', Accidental.GetName('b', 'zh'))
        self.assertEqual('重降', Accidental.GetName('bb', 'zh'))
        self.assertEqual('降*3', Accidental.GetName('bbb', 'zh'))


if __name__ == '__main__':
    unittest.main()
