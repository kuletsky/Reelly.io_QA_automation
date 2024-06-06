# Created by costa at 6/6/24
Feature: Tests for user profile page
  All testing scenarios for user profile page are located here

  Scenario: User can select different roles
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page kuletsky@gmail.com, bJyxsHf5Y@6dnEV
    When Click on "Settings" option at the left side menu
    When Click on "Edit profile" option
    Then Verify that Profile page opened
    When Select Developer role
    Then Verify that Developer role selected

  Scenario: User can select different position
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page kuletsky@gmail.com, bJyxsHf5Y@6dnEV
    When Click on "Settings" option at the left side menu
    When Click on "Edit profile" option
    Then Verify that Profile page opened
    When Select Director / CEO position
    Then Verify that Director / CEO position selected