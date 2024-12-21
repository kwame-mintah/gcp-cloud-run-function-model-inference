Feature: Make a prediction providing various wine features

  Scenario Outline: A user should be able to make a wine prediction
    Given a user has wine quantitative features for prediction
      | alcohol | chlorides | citric acid | density | fixed acidity | free sulfur dioxide | pH   | residual sugar | sulphates | total sulfur dioxide | volatile acidity |
      | 12.8    | 0.029     | 0.48        | 0.98    | 6.2           | 29                  | 3.33 | 1.2            | 0.39      | 75                   | 0.66             |
    Then they make a prediction against <url>
    And the response status code should be <status>
    Examples:
      | url      | status |
      | /predict/ | 200    |
