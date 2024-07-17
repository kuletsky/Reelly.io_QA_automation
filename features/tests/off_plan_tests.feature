# Created by costa at 7/8/24
Feature: Tests for Off-plan page
  All testing scenarios for Off-plan page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

  Scenario: Verify that all projects are shown
    When Click on Main page "Off-plan"
    Then Verify that all projects on Off-plan are shown

  Scenario: Verify that user can click on Top Menu "Map view"
    When Click on Main page "Off-plan"
    When Click on top Menu "Map view"
    Then Verify that URL of window contains map

  Scenario: Verify that user can click on Top Menu "Secondary"
    When Click on Main page "Off-plan"
    When Click on top Menu "Secondary"
    Then Verify that URL of window contains secondary-listings
    And Verify that all projects on Secondary are shown

  Scenario: Verify that user can click on Top Menu "My listings"
    When Click on Main page "Off-plan"
    When Click on top Menu "My listings"
    Then Verify that URL of window contains my-secondary-listings
    And Verify that all projects on Secondary are shown