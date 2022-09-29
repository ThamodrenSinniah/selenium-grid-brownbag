Feature: Check VSM Login Page

  Background: At VSM Login Page
    When I am at VSM Login Page

  Scenario: Check if Title is correct
    Then I see title is "Dürr Dental Login"

  Scenario: Check Password Forgot
    When I click Password Forgotten
    Then I see Password Reset Page

  Scenario: Check Contact Details
    Then I see Contact Number is "+49 7142 / 705-0"
      And I see Contact Email is "info@duerrdental.com"