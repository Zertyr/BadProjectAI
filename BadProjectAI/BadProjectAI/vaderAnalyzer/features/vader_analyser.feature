Feature: vader_analyser

    Scenario : A user put a positive string in the tchat and we answer with a positive feelings

        Given a positive string chain

        When start vader function

        Then analyser send a "positive sentiment"

    Scenario: A user put a negative string chain in the tchat and we answer with a negative feelings
 
        Given a negative string chain
    
        When start vader function
    
        Then analyser send "negative sentiment"
    
    Scenario: A user put a neutral string chain in the tchat and we answer with a mixed feelings
 
        Given a neutral string chain
    
        When start vader function
    
        Then analyzer send "neutral sentiment"