Feature: practicetestautomation

  Background: common steps
    Given launch chrome browser
    When open login page
    Then verify logo present on page
    And Enter username "student" and password "Password123"
    And verify login

  Scenario: navigate practice page
    And Navigate to practice page

  Scenario: navigate home page
    And Navigate to home page
