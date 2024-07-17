# Created by costa at 7/4/24
Feature: Tests for Main page
  All testing scenarios for Main page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

  Scenario: Verify the user can click on “Connect the company” on the left side of the main page
    Given Store original window
    When Click on Main page "Connect the company"
    When Switch to the new window
    Then Verify that URL of window contains book-presentation

  Scenario: Verify the user can click on “App Store” on the left side of the main page
    When Click on Main page "App Store"
    Then Verify that URL of window contains apps.apple.com

  Scenario: Verify the user can click on “Android” on the left side of the main page
    When Click on Main page "Android"
    Then Verify that URL of window contains play.google.com

  Scenario: Verify the user can click on “Off-plan” on the left menu of the main page
    When Click on Main page "Off-plan"
    Then Verify that URL of window contains soft.reelly.io

  Scenario: Verify the user can click on “Secondary” on the left menu of the main page
    When Click on Main page "Secondary"
    Then Verify that URL of window contains secondary-listings

  Scenario: Verify the user can click on “Calendar” on the left menu of the main page
    When Click on Main page "Calendar"
    Then Verify that URL of window contains calendar

  Scenario: Verify the user can click on “Referral” on the left menu of the main page
    When Click on Main page "Referral "
    Then Verify that URL of window contains referral

  Scenario: Verify the user can click on “University” on the left menu of the main page
    When Click on Main page "University"
    Then Verify that URL of window contains university

  Scenario: Verify the user can click on “Market” on the left menu of the main page
    When Click on Main page "Market"
    Then Verify that URL of window contains market

