from matplotlib import pyplot as plt
from wordcloud import WordCloud

text= open("english.txt",encoding="utf8").read()
wordcloud = WordCloud(max_font_size=40).generate(text)
wordcloud.to_file("result_english.jpg")