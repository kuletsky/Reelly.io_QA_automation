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

  Scenario: Verify user can see "Total Projects" on Off-plan page
    When Click on Main page "Off-plan"
    Then Verify "Total Projects" displays accurate project count

  Scenario Outline: Verify "Total Projects" Count Updates with Location Filter Change
    When Click on Main page "Off-plan"
    When Change Location <filter>
    Then Verify "Total Projects" Count Updates with Location Filter Change
    Examples:
    |filter   |
    |Dubai    |
    |Bali     |
    |Abu Dhabi|
    |Ajman    |
    |Sharjah  |
    |Thailand |
    |Oman     |

  Scenario: Verify user can open the Off plan page and go through the pagination
    When Click on Main page "Off-plan"
    Then Verify the right page opens Off-plan
    When Go to the final page using the pegination button and back on Off-plan