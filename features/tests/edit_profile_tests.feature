# Created by costa at 6/6/24
Feature: Tests for user profile page
  All testing scenarios for user profile page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page kuletsky@gmail.com, bJyxsHf5Y@6dnEV

  Scenario: User can select different roles
    When Click on "Settings" option at the left side menu
    When Click on "Edit profile" option
    Then Verify that Profile page opened
    When Select Broker role
    Then Verify that Broker option selected

  Scenario: User can select different position
    When Click on "Settings" option at the left side menu
    When Click on "Edit profile" option
    Then Verify that Profile page opened
    When Select Director / CEO position
    Then Verify that Director / CEO option selected

  @mobile_web
  Scenario: MOB_WEB User can select different roles
    When Click on "Menu"
    When Click on "Edit profile" option
    Then Verify that Profile page opened
    When Select Broker role
    Then Verify that Broker option selected

  @mobile_web
  Scenario: MOB_WEB User can select different position
    When Click on "Menu"
    When Click on "Edit profile" option
    Then Verify that Profile page opened
    When Select Director / CEO position
    Then Verify that Director / CEO option selected