import MeCab
import collections

text= open("sample.txt",encoding="utf8").read()
#mecab = MeCab.Tagger("-Owakati")#辞書を指定
mecab = MeCab.Tagger()
mecab.parse('')
node = mecab.parseToNode(text)
 
# print(node)
print(mecab.parse(text))

word_list=[]
while node:
    word_list.append(node.surface)
    node=node.next
word_chain=' '.join(word_list)

count = collections.Counter(word_list)
print(count.most_common(20))    

    
    







