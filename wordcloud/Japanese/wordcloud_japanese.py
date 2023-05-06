from matplotlib import pyplot as plt
from wordcloud import WordCloud
import MeCab
import collections

text= open("japanese.txt",encoding="utf8").read()

# mytext ="ロシア大統領府は、プーチン大統領を狙って首都モスクワのクレムリンをウクライナの無人機が攻撃しようとしたと主張し、報復措置をとると発表しました。これに対しウクライナのゼレンスキー大統領は「われわれがプーチン大統領やモスクワを攻撃することはない」と述べて関与を否定しました。"
#mecab = MeCab.Tagger("-Owakati")#辞書を指定
mecab = MeCab.Tagger()
mecab.parse('')
node = mecab.parseToNode(text)

word_list=[]
while node:
    word_list.append(node.surface)
    node=node.next
word_chain=' '.join(word_list)
print(word_chain)
print(type(word_chain))

WORDCLOUD_FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"
WORDCLOUD_WIDTH = 600
WORDCLOUD_HEIGHT = 600
WORDCLOUD_BG_COLOR = 'white'

wordcloud = WordCloud(
    font_path=WORDCLOUD_FONT_PATH,
    max_font_size=40,
    width = WORDCLOUD_WIDTH,
    height = WORDCLOUD_HEIGHT,
    background_color = WORDCLOUD_BG_COLOR
    ).generate(word_chain)
wordcloud.to_file("result_japanese.jpg")

count = collections.Counter(word_list)
print(count.most_common(20)) 