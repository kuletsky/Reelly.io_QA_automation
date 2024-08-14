# Created by costa at 8/13/24
Feature: Tests for user guide page
  All testing scenarios for user quide page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

    Scenario: User can open User guide page
      When Click on "Settings" option at the left side menu
      And Click on "User Guide" option
      Then Verify that URL of window contains user-guide