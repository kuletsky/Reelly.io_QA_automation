# Created by costa at 5/31/24
Feature: Tests for user settings page
  All testing scenarios for user settings page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

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