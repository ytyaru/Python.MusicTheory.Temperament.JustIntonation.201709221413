#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#各種音階における音程
class ScaleIntervals:
    #===一般===
    #7音
    Major = (2,2,1,2,2,2)#(2,2,1,2,2,2,1)
    Minor = (2,1,2,2,1,2)#(2,1,2,2,1,2,2)
    Diminished = (2,1,2,1,2,1)#(2,1,2,1,2,1,2)
    HarmonicMinor = (2,1,2,2,1,2)#(2,1,2,2,1,2,3)
    MelodicMinor = (2,1,2,2,1,3)#(2,1,2,2,1,3,2)
    #5音
    MajorPentaTonic = (2,2,2,2)
    MinorPentaTonic = (3,2,2,3)
    #6音
    BlueNote = (3,2,1,1,3)
    #12音
    Chromatic = tuple(*[[1]*11])
    #移調の限られた旋法
    Tcherepnin = (2,1,1,2,1,1,2,1,1)#移調の限られた旋法第3旋法
    WholeTone = (2,2,2,2,2,2,2)# キーがC, C#のときしか使えないスケール
    
    # ===民族===
    ClassicJapan = ((2,2,3,2),(2,3,2,2),(2,3,2,3),(1,4,2,3),(4,1,2,4)) #('呂旋法', '律旋法', '陽旋法・田舎節', '陰旋法・都節', '琉球音階')
    YonanukiJapan = ((2,2,3,2),(2,1,3,1),(3,2,2,3),(4,1,2,4),(2,1,4,2),(1,4,1,4)) #('ヨナ抜き長音階', 'ヨナ抜き短音階', 'ニロ抜き短音階', 'ニロ抜き長音階', '雲井音階', '岩戸音階')
#    ArabicMaqam = ((2,2-1/4,1+3/4,2,2,1-1/4),) # (1/4音さげるのを表現できない)半音の半分、1/4音下げる記号をここではqと表記する事にする 	C D Eq F G A Bq  	1 2 q3 4 5 6 7
    ArabicMaqam = ((None, None, 'q', None, None, None, 'q'),#1/4音下げる記号をqと表記する。C,D,E,F,G,A,Bを基準とする
                (None, None, 'b', None, None, 'b', None),
                (None, None, 'b', '#', None, 'b', None),
                (None, None, 'b', '#', None, None, 'b'),
                (None, 'b', None, None, None, 'b', None),
                (None, 'q', 'b', None, None, 'b', 'b'),
                (None, 'q', 'b', 'b', None, 'b', 'b'),
                (None, 'b', None, None, None, 'b', 'b'),
                ('Eq', 'F', 'G', 'A', 'Bq', 'C', 'D'),
                ('Eq', 'F', 'G', 'Ab', 'B', 'C', 'D'),
                ) 
    Chaina = (2,2,3,2)# (1/4音さげるのを表現できない)('宮調式', '商調式', '角調式', '徴調式', '羽調式')
    Gypsy = (1,3,1,2,1,3)
    Hungary = (2,1,3,1,2,2)
    Pelog = ((1,2,4,1)) #(1/4音さげるのを表現できない)
    Spain = (1,2,1,1,2,1,2)#フリジアン・スケールにMajor 3rdを加えたスケール


if __name__ == '__main__':
    print('========== 一般スケール ==========')
    print('----- 7音 -----')
    print(ScaleIntervals.Major)
    print(ScaleIntervals.Minor)
    print(ScaleIntervals.Diminished)
    print(ScaleIntervals.HarmonicMinor)
    print(ScaleIntervals.MelodicMinor)
    print('----- 5音 -----')
    print(ScaleIntervals.BlueNote)
    print(ScaleIntervals.MajorPentaTonic)
    print(ScaleIntervals.MinorPentaTonic)
    print('----- 12音 -----')
    print(ScaleIntervals.Chromatic)
    print('----- 移調の限られた旋法 -----')
    print(ScaleIntervals.Tcherepnin)
    print(ScaleIntervals.WholeTone)
    print('========== 民族スケール ==========')
    print(ScaleIntervals.ClassicJapan)
    print(ScaleIntervals.YonanukiJapan)
    print(ScaleIntervals.ArabicMaqam)
    print(ScaleIntervals.Chaina)
    print(ScaleIntervals.Gypsy)
    print(ScaleIntervals.Hungary)
    print(ScaleIntervals.Pelog)
    print(ScaleIntervals.Spain)
    print(ScaleIntervals.Major)
    print(ScaleIntervals.Major)
    print(ScaleIntervals.Major)
    print(ScaleIntervals.Major)
    print(ScaleIntervals.Major)
    print(ScaleIntervals.Major)

