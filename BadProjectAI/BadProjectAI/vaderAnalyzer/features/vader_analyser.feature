# Fichier : features/vader_analyser.feature

Feature: Analyseur de sentiments VADER

Scenario: Un utilisateur entre une chaîne de caractères positive dans le tchat et nous répondons avec des sentiments positifs
    Given une chaîne de caractères positive
    When l'utilisateur démarre la fonction VADER
    Then l'analyseur envoie sentiment

Scenario: Un utilisateur entre une chaîne de caractères négative dans le tchat et nous répondons avec des sentiments négatifs
    Given une chaîne de caractères négative
    When l'utilisateur démarre la fonction VADER
    Then l'analyseur envoie sentiment

Scenario: Un utilisateur entre une chaîne de caractères neutre dans le tchat et nous répondons avec des sentiments mixtes
    Given une chaîne de caractères neutre
    When l'utilisateur démarre la fonction VADER
    Then l'analyseur envoie sentiment