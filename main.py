# from textblob import TextBlob
# from newspaper import Article

# # pip install nltk
# # pip install textblob
# # pip install newspaper3k

# url = 'https://www.worldwildlife.org/magazine/issues/spring-2015/articles/turn-off-your-lights-for-earth-hour'
# article = Article(url)

# article.download()
# article.parse()
# article.nlp()

# text = article.summary
# print(text)

# blob = TextBlob(text)
# sentiment = blob.sentiment.polarity # -1 to 1   
# print(sentiment)


# from newspaper import Article
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# text = "https://abcnews.go.com/US/timeline-shooting-texas-elementary-school-unfolded/story?id=84966910&fbclid=IwAR0a3z6Nmq3Qnl-gWg6jDQthj-CfHVNjG7oTYNTHZoqEAyVmxE4VFqEbpu8"


# article = Article(text)
# article.download()
# article.parse()
# article.nlp()


# f = article.summary

# print(f)
# analyzer = SentimentIntensityAnalyzer()
# vs = analyzer.polarity_scores(f)
# print(vs)


from newspaper import Article
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import googletrans
from googletrans import Translator
import Text2Emotion as te
import nltk
import pygal
pie_chart = pygal.Pie()
nltk.download("vader_lexicon")

nltk.download('omw-1.4')
text = "Maganda ang kita sa ating napiling negosyo. 👉🥺👈"
translator = Translator()

source_lan = "tl"
translated_to= "en"



translated_text = translator.translate(text, src=source_lan, dest = translated_to)

analyzer = SentimentIntensityAnalyzer()
vs = analyzer.polarity_scores(translated_text.text)
print(translated_text.text)

analyzeem=te.get_emotion(translated_text.text)



for key, value in analyzeem.items():
    pie_chart.add(key, value)
    
pie_chart.title = 'Pie chart' 
pie_chart.render_to_file("result.svg")
print(analyzeem)
print(vs)