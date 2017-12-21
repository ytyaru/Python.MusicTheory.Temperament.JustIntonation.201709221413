#!python3.6
import unittest
from MusicTheory.pitch.Key import Key
from MusicTheory.pitch.Accidental import Accidental
import Framework.ConstMeta
"""
Keyのテスト。
"""
class TestKey(unittest.TestCase):
    def test_Keys(self): self.assertEqual(tuple('CDEFGAB'), Key.Keys)
    def test_Perfects_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            Key.Keys = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))
    def test_PitchClasses(self): self.assertEqual((0,2,4,5,7,9,11), Key.PitchClasses)
    def test_PitchClasses_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            Key.PitchClasses = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))
    def test_KeyNames(self):
        self.assertEqual({
            'en':tuple('CDEFGAB'),
            'ja':tuple('ハニホヘトイロ'), 
            'de':tuple('CDEFGAH'), 
            'it':tuple('Do,Re,Mi,Fa,Sol,La,Si'.split(',')), 
            'fr':tuple('Ut,Ré,Mi,Fa,Sol,La,Si'.split(',')),
            'es':tuple('Do,Re,Mi,Fa,Sol,La,Si'.split(',')),
            'zh':tuple('CDEFGAB'), 
        }, Key.KeyNames)
    def test_KeyNames_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            Key.KeyNames = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))
    def test_KeyNames_NotSet_dict(self):
        with self.assertRaises(Framework.ConstDict.ConstDict.ConstError) as e:
            Key.KeyNames['en'] = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))
    def test_Get(self):
        keys = {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11}
        for key, pitch_class in keys.items():
            with self.subTest(key=key):
                self.assertEqual(pitch_class, Key.Get(key))
    
    def test_Get_Accidental(self):
        keys = {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11}
        for k, kp in keys.items():
            for acc_count in range(1, 4):
                for a, ap in Accidental.Accidentals.items():
                    key = k + a*acc_count
                    pitch = kp + (ap*acc_count)
                    with self.subTest(key=key):
                        self.assertEqual(pitch, Key.Get(key))
    
    def test_Get_int(self):
        with self.assertRaises(TypeError) as e:
            Key.Get(100)
        self.assertIn('引数nameはstr型にしてください。', str(e.exception))

    def test_Get_Invalid(self):
        with self.assertRaises(ValueError) as e:
            Key.Get('無効値')
        self.assertIn('keyは次のうちのいずれかにしてください。', str(e.exception))

    def test_Get_Bad_Combination(self):
        with self.assertRaises(ValueError) as e:
            Key.Get('c#')
        self.assertIn('keyは次のうちのいずれかにしてください。', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Key.Get('CC')
        self.assertIn('引数accidentalに使える文字は次のものだけです。', str(e.exception))

    def test_GetName_en(self):
        names = Key.KeyNames['ja']
        for i,key in enumerate(Key.Keys):
            self.assertEqual(names[i], Key.GetName(key, 'ja'))
            self.assertEqual('嬰'+names[i], Key.GetName(key+'#', 'ja'))
            self.assertEqual('変'+names[i], Key.GetName(key+'b', 'ja'))
            self.assertEqual('重嬰'+names[i], Key.GetName(key+'##', 'ja'))
            self.assertEqual('重変'+names[i], Key.GetName(key+'bb', 'ja'))
            self.assertEqual('嬰*3'+names[i], Key.GetName(key+'###', 'ja'))
            self.assertEqual('変*3'+names[i], Key.GetName(key+'bbb', 'ja'))
    def test_GetName_en(self):
        names = Key.KeyNames['en']
        for i,key in enumerate(Key.Keys):
            self.assertEqual(names[i], Key.GetName(key, 'en'))
            self.assertEqual(names[i]+' sharp', Key.GetName(key+'#', 'en'))
            self.assertEqual(names[i]+' flat', Key.GetName(key+'b', 'en'))
            self.assertEqual(names[i]+' double sharp', Key.GetName(key+'##', 'en'))
            self.assertEqual(names[i]+' double flat', Key.GetName(key+'bb', 'en'))
            self.assertEqual(names[i]+' sharp*3', Key.GetName(key+'###', 'en'))
            self.assertEqual(names[i]+' flat*3', Key.GetName(key+'bbb', 'en'))
    def test_GetName_de(self):
        names = Key.KeyNames['de']
        for i,key in enumerate(Key.Keys):
            self.assertEqual(names[i], Key.GetName(key, 'de'))
            self.assertEqual(names[i]+' is', Key.GetName(key+'#', 'de'))
            self.assertEqual(names[i]+' es', Key.GetName(key+'b', 'de'))
            self.assertEqual(names[i]+' isis', Key.GetName(key+'##', 'de'))
            self.assertEqual(names[i]+' eses', Key.GetName(key+'bb', 'de'))
            self.assertEqual(names[i]+' is*3', Key.GetName(key+'###', 'de'))
            self.assertEqual(names[i]+' es*3', Key.GetName(key+'bbb', 'de'))
    def test_GetName_it(self):
        names = Key.KeyNames['it']
        for i,key in enumerate(Key.Keys):
            self.assertEqual(names[i], Key.GetName(key, 'it'))
            self.assertEqual(names[i]+' diesis', Key.GetName(key+'#', 'it'))
            self.assertEqual(names[i]+' bemolle', Key.GetName(key+'b', 'it'))
            self.assertEqual(names[i]+' doppio diesis', Key.GetName(key+'##', 'it'))
            self.assertEqual(names[i]+' doppio bemolle', Key.GetName(key+'bb', 'it'))
            self.assertEqual(names[i]+' diesis*3', Key.GetName(key+'###', 'it'))
            self.assertEqual(names[i]+' bemolle*3', Key.GetName(key+'bbb', 'it'))
    def test_GetName_fr(self):
        names = Key.KeyNames['fr']
        for i,key in enumerate(Key.Keys):
            self.assertEqual(names[i], Key.GetName(key, 'fr'))
            self.assertEqual(names[i]+' dièse', Key.GetName(key+'#', 'fr'))
            self.assertEqual(names[i]+' bémol', Key.GetName(key+'b', 'fr'))
            self.assertEqual(names[i]+' double dièse', Key.GetName(key+'##', 'fr'))
            self.assertEqual(names[i]+' double bémol', Key.GetName(key+'bb', 'fr'))
            self.assertEqual(names[i]+' dièse*3', Key.GetName(key+'###', 'fr'))
            self.assertEqual(names[i]+' bémol*3', Key.GetName(key+'bbb', 'fr'))
    def test_GetName_es(self):
        names = Key.KeyNames['es']
        for i,key in enumerate(Key.Keys):
            self.assertEqual(names[i], Key.GetName(key, 'es'))
            self.assertEqual(names[i]+' sostenido', Key.GetName(key+'#', 'es'))
            self.assertEqual(names[i]+' bemol', Key.GetName(key+'b', 'es'))
            self.assertEqual(names[i]+' sostenido doble', Key.GetName(key+'##', 'es'))
            self.assertEqual(names[i]+' bemol doble', Key.GetName(key+'bb', 'es'))
            self.assertEqual(names[i]+' sostenido*3', Key.GetName(key+'###', 'es'))
            self.assertEqual(names[i]+' bemol*3', Key.GetName(key+'bbb', 'es'))
    def test_GetName_zh(self):
        names = Key.KeyNames['zh']
        for i,key in enumerate(Key.Keys):
            self.assertEqual(names[i], Key.GetName(key, 'zh'))
            self.assertEqual('升'+names[i], Key.GetName(key+'#', 'zh'))
            self.assertEqual('降'+names[i], Key.GetName(key+'b', 'zh'))
            self.assertEqual('重升'+names[i], Key.GetName(key+'##', 'zh'))
            self.assertEqual('重降'+names[i], Key.GetName(key+'bb', 'zh'))
            self.assertEqual('升*3'+names[i], Key.GetName(key+'###', 'zh'))
            self.assertEqual('降*3'+names[i], Key.GetName(key+'bbb', 'zh'))


if __name__ == '__main__':
    unittest.main()
