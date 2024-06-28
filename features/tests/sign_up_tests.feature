# Created by costa at 6/25/24
Feature: Tests for Sign Up page
  All testing scenarios for Sign Up page are located here

  Scenario: Verify user can enter the information into the input fields on the registration page
    Given Open the main page
    When Click on the "Open in browser"
    When Click on the "Create account"
    When Fill in the Full name Tester
    When Fill in random Phone
    When Fill in random Email
    When Fill in random PSW
    When Fill in random Website
    When Select Broker roles
    When Select Seller / Manager position
    When Select country Germany
    When Select your company size 500+
    When Click "Create account"
    When Click on "Settings" option at the left side menu
    When Click on "Edit profile" option
    Then Verify the right User is present