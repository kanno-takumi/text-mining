import MeCab
import collections

mytext ="ロシア大統領府は、プーチン大統領を狙って首都モスクワのクレムリンをウクライナの無人機が攻撃しようとしたと主張し、報復措置をとると発表しました。これに対しウクライナのゼレンスキー大統領は「われわれがプーチン大統領やモスクワを攻撃することはない」と述べて関与を否定しました。"
#mecab = MeCab.Tagger("-Owakati")#辞書を指定
mecab = MeCab.Tagger()
mecab.parse('')
node = mecab.parseToNode(mytext)
 
# print(node)
print(mecab.parse(mytext))

word_list=[]
while node:
    word_list.append(node.surface)
    node=node.next
word_chain=' '.join(word_list)

count = collections.Counter(word_list)
print(count.most_common(20))    

    
    







