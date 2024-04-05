from aloe import before, step, world
from aloe.tools import guess_types
from aloe_django.steps.models import get_model
from vaderSentiment import SentimentIntensityAnalyzer

chain: str = ""
analyzer = SentimentIntensityAnalyzer()
score = 0
result = ""

@step('a positive string chain')
def step_positive_chain(self):
    chain = "The book was good"

@step('a negatif string chain')
def step_negatif_chain(self):
    chain = "Today SUX!"

@step('a neutral string chain')
def step_neutral_chain(self):
    chain = "Today only kinda sux! But I'll get by, lol"

@step('start vader function')
def vader_function(self):
    score = analyzer.polarity_scores(chain)

@step('analyzer send "([^"]+)" ')
def step_create_users(self):
    if score >= 0.05:
        result = "positive sentiment"
    elif score <= -0.05:
        result = "negative sentiment"
    else:
        result = "neutral sentiment"

