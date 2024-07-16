Feature: practicetestautomation_multipleinputs

  Scenario Outline: Logo presence on login page
    Given launch chrome browser
    When open login page
    Then verify logo present on page
    And Enter username "<username>" and password "<password>"
    And verify login

    Examples:
      | username | password     |
      | adm      | hiuho8       |
      | admin    | hiuho8oo     |
      | student  | Password123  |
      | admn     | hiuho89      |
