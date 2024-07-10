# Created by costa at 5/31/24
Feature: Tests for user settings page
  All testing scenarios for user settings page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page kuletsky@gmail.com, bJyxsHf5Y@6dnEV

  @smoke
  Scenario: User can access Whatsapp and Telegram communities
    When Click on "Settings" option at the left side menu
    Given Store original window
    When Click on "Support" option
    When Switch to the new window
    Then Verify that URL of window contains api.whatsapp.com
    When Close current page
    And Go back to original window
    And Click on "News" option
    Then Verify that URL of window contains t.me

  Scenario: User can go to settings and edit the personal information
    When Click on "Settings" option at the left side menu
    And Click on "Edit profile" option
    And Fill in the Full name Tester
    And Fill in random Phone
    And Fill in random Email
    And Fill in random PSW
    And Fill in random Company website
    And Select Broker roles
    And Select Seller / Manager position
    And Select country Germany
    And Select your company size 500+


  @mobile_web
  Scenario: MOB_WEB User can access Whatsapp and Telegram communities
    When Click on "Menu"
    Given Store original window
    When Click on "Support" option
    When Switch to the new window
    Then Verify that URL of window contains api.whatsapp.com
    When Close current page
    When Go back to original window
    When Click on "News" option
    Then Verify that URL of window contains t.me