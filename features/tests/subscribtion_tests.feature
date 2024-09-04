Feature: Tests for subscription page
  All testing scenarios for subscription page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

  Scenario: User can open Subscription & payments page
    When Click on "Settings" option at the left side menu
    And Click on "Subscription & payments" option
    Then Verify that URL of window contains subscription
    And Verify title “Subscription & payments” is visible
    And Verify “back” and “upgrade plan” buttons are available