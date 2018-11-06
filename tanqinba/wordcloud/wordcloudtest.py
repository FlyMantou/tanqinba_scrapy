import re
import jieba.analyse as analyse
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
comments = []
cleaned_comments = ''
def filterComments():
    cleaned_comments = ''
    with open('3.txt', 'r', encoding='utf8') as f:
        for line in f:
            comments.append(line)
    for k in range(len(comments)):
        cleaned_comments = cleaned_comments + (str(comments[k])).strip()
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, cleaned_comments)
    cleaned_comments = ''.join(filterdata)
    return  cleaned_comments


cleaned_comments = filterComments()
analyse.set_stop_words("stopwords.txt")
#withWeight=True为显示字符出现的频率，格式为[('aa',0.23),('a',0.11)]
#不加这个参数，或者参数值为false的时候格式为['a','b']
words_df = analyse.extract_tags(cleaned_comments,topK=100,withWeight=True)
back_coloring = imread('1.jpg')
wordcloud =  WordCloud( font_path='C:\Windows\Fonts\simhei.ttf',#设置字体
                        background_color="black", #背景颜色
                        max_words=2000,# 词云显示的最大词数
                        mask=back_coloring,#设置背景图片
                        max_font_size=100, #字体最大值
                        random_state=42,
                        )
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(back_coloring)

#generate和generate_from_text接受的为文本，例'a b c d'
#generat参数为以分隔符比如空格隔开的字符串
#words = " ".join(words_df)
#wordcloud.generate(words)
#wordcloud.generate_from_text(words)
#有频率的时候用generate_from_frequencies,fit_words
#generate_from_frequencies接受的参数为字典，注意必须为字典可以直接使用结巴分词带频率的结果
#wordcloud.generate_from_frequencies(dict(words_df))
wordcloud.fit_words(dict(words_df))

#plt.imshow(wordcloud.recolor(color_func=image_colors))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
