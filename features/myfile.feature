Feature: practicetestautomation
  Scenario: Logo presence on login page
    Given launch chrome browser
    When open login page
    Then verify logo present on page
    And Enter username "student" and password "Password123"
    And verify login



