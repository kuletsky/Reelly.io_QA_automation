Feature: Tests for user change password page
  All testing scenarios for change password page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

  Scenario: User can open change password page
    When Click on "Settings" option at the left side menu
    And Click on "Change password" option
    Then Verify that URL of window contains set-new-password
    When Add some test password to the input fields
    Then Verify the “Change password” button is available
