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
