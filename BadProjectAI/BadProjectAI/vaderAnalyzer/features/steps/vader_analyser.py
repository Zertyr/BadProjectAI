# Fichier : features/steps/vader_steps.py

from behave import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#from vaderSentiment import SentimentIntensityAnalyzer

chain: str = ""
analyzer = SentimentIntensityAnalyzer()
score = 0
result = ""

from behave import given, when, then

@given("une chaîne de caractères positive")
def step_given_positive_string(context):
    context.string_chain = "VADER is smart, handsome, and funny."
    context.expected_sentiment = "positive sentiment"
    pass

@given("une chaîne de caractères négative")
def step_given_negative_string(context):
    context.string_chain = "VADER is not smart, handsome, nor funny."
    context.expected_sentiment = "negative sentiment"
    pass

@given("une chaîne de caractères neutre")
def step_given_neutral_string(context):
    context.string_chain = "C'est une journée ordinaire."
    context.expected_sentiment = "neutral sentiment"
    pass

@when("l'utilisateur démarre la fonction VADER")
def step_when_start_vader_function(context):
    context.sentiment = analyzer.polarity_scores(context.string_chain)
    if context.sentiment['compound'] >= 0.05:
        context.result = "positive sentiment"
    elif context.sentiment['compound'] <= -0.05:
        context.result = "negative sentiment"
    else:
        context.result = "neutral sentiment"
    pass

@then("l'analyseur envoie sentiment")
def step_then_analyzer_send_sentiment(context):
    assert context.result == context.expected_sentiment, f"Le sentiment attendu était {context.expected_sentiment}, mais le sentiment obtenu était {context.result}"
    pass
