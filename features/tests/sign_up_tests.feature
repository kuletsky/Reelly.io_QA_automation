# Created by costa at 6/25/24
Feature: Tests for Sign Up page
  All testing scenarios for Sign Up page are located here

  Scenario: Verify user can enter the information into the input fields on the registration page
    Given Open the main page
    When Click on the "Open in browser"
    When Click on the "Create account"
    When Fill in the Full name
    When Fill in Phone
    When Fill in Email
    When Fill in psw
    When Select <string> role
    When Select <string> position
    When Select country
    When Select your company size
    When Click "Create account"
    Then Verify the right information is present