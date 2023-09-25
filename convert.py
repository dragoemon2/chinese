import pypinyin

words="""
东京 東京
中国 中国
香港 香港
深圳 深圳
台湾 台湾
德国 ドイツ
朝鲜 朝鮮
福建 福建
北京 北京
美国 アメリカ
蒙古 モンゴル
武汉 武漢
四川 四川
澳门 モンゴル
日本 日本
印度 インド
"""

for line in words.split("\n"):
    if line == "": continue
    word, meaning = line.split()
    pin = ''.join([pins[0] for pins in pypinyin.pinyin(word, heteronym=True)])
    print(f'"{word}","{pin}","{meaning}",zh-CN,zh-CN')