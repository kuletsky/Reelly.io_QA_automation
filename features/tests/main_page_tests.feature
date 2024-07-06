# Created by costa at 7/4/24
Feature: Tests for Main page
  All testing scenarios for Main page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page kuletsky@gmail.com, bJyxsHf5Y@6dnEV

  Scenario: Verify the user can click on “Connect the company” on the left side of the main page
    Given Store original window
    When Click on "Connect the company"
    When Switch to the new window
    Then Verify that URL of window contains book-presentation

  Scenario: Verify the user can click on “App Store” on the left side of the main page
    When Click on "App Store"
    Then Verify that URL of window contains apps.apple.com