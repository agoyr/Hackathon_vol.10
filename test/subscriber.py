import os
import pandas as pd
from path_info import DATA_DIR

# データをリストに変換
data = [
    ['北海道', 65810, 111800, 177610],
    ['青森', 10915, 23650, 34565],
    ['岩手', 10980, 23825, 34805],
    ['宮城', 30120, 52450, 82570],
    ['秋田', 9070, 14960, 24030],
    ['山形', 10720, 21105, 31825],
    ['福島', 10720, 21105, 31825],
    ['茨城', 27805, 59480, 87285],
    ['栃木', 22520, 42905, 65425],
    ['群馬', 23220, 42460, 65680],
    ['埼玉', 81440, 148290, 229640],
    ['千葉', 72630, 111150, 183780],
    ['東京', 228740, 300505, 529280],
    ['神奈川', 115135, 198300, 313435],
    ['新潟', 22335, 40695, 63035],
    ['富山', 11690, 23410, 35100],
    ['石川', 15060, 27450, 42510],
    ['福井', 8980, 16605, 25585],
    ['山梨', 8120, 16145, 24265],
    ['長野', 21740, 40240, 61980],
    ['岐阜', 22965, 40470, 63435],
    ['静岡', 38870, 78290, 117160],
    ['愛知', 109990, 197030, 307040],
    ['三重', 20735, 36070, 56805],
    ['滋賀', 20735, 36070, 56805],
    ['京都', 41085, 62875, 103960],
    ['大阪', 162945, 209600, 372545],
    ['兵庫', 73635, 110950, 184585],
    ['奈良', 18505, 24920, 43425],
    ['和歌山', 9050, 16090, 25590],
    ['鳥取', 5625, 10735, 16360],
    ['島根', 6525, 12220, 18745],
    ['岡山', 26945, 42685, 69630],
    ['広島', 38065, 65460, 103525],
    ['山口', 13015, 27410, 40425],
    ['徳島', 8490, 13415, 21905],
    ['香川', 11630, 22795, 34425],
    ['愛媛', 13985, 26035, 40020],
    ['高知', 6935, 11295, 17590],
    ['福岡', 78015, 125850, 203865],
    ['佐賀', 7765, 14190, 21955],
    ['長崎', 12280, 24160, 36440],
    ['熊本', 21150, 33730, 55560],
    ['大分', 11895, 24395, 36290],
    ['宮崎', 11150, 21210, 32360],
    ['鹿児島', 11150, 21210, 32360],
    ['沖縄', 17745, 28115, 45860],
]

# データフレームに変換
df = pd.DataFrame(data, columns=['都道府県', '女性', '男性', '合計'])

result_path = DATA_DIR

# CSVファイルに保存
df.to_csv(os.path.join(result_path, 'pairs_membership_by_prefecture.csv'), index=False)
