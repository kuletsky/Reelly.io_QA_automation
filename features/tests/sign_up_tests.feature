# Created by costa at 6/25/24
Feature: Tests for Sign Up page
  All testing scenarios for Sign Up page are located here

  Scenario: Verify the right information is present into the input fields on the registration page
    Given Open the main page
    When Click on the "Open in browser"
    And Click on the "Create account"
    And Fill in the Full name Tester
    And Fill in random Phone
    And Fill in random Email
    And Fill in random PSW
    And Fill in random Company website
    And Select Broker roles
    And Select Seller / Manager position
    And Select country Germany
    And Select your company size 500+
    And Click "Create account"
    And Click on "Settings" option at the left side menu
    And Click on "Edit profile" option
    Then Verify the right information is present into the input fields on the registration page
#    And Verify the right User name
#    And Verify the right Phone number
#    And Verify the right Company website
#    And Verify the Email