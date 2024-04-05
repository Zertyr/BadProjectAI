from behave import *

#from vaderSentiment import SentimentIntensityAnalyzer

chain: str = ""
#analyzer = SentimentIntensityAnalyzer()
score = 0
result = ""

@given('a positive string chain')
def step_positive_chain(context):
    chain = "The book was good"

@given('a negatif string chain')
def step_negatif_chain(context):
    chain = "Today SUX!"

@given('a neutral string chain')
def step_neutral_chain(context):
    chain = "Today only kinda sux! But I'll get by, lol"

@when('start vader function')
def vader_function(context):
 #   score = analyzer.polarity_scores(chain)
    pass

@then('analyzer send "([^"]+)" ')
def step_create_users(context):
    if score >= 0.05:
        result = "positive sentiment"
    elif score <= -0.05:
        result = "negative sentiment"
    else:
        result = "neutral sentiment"

