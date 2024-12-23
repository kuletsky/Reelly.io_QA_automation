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
      | filter    |
      | Dubai     |
      | Bali      |
      | Abu Dhabi |
      | Ajman     |
      | Sharjah   |
      | Thailand  |
      | Oman      |

  Scenario: Verify user can open the Off plan page and go through the pagination
    When Click on Main page "Off-plan"
    Then Verify the right page opens Off-plan
    And Verify pagination to final page of Off-plan
    And Verify pagination to first page of Off-plan

  Scenario: Verify user can filter the Off plan by Unit price range
    When Click on Main page "Off-plan"
    Then Verify the right page opens Off-plan
    When Click on Filters on Off-plan
    When Filter the price of products range from 1200000 to 2000000 AED
    Then Verify the price in all cards is inside the range off-plan

  Scenario: User can see titles and pictures on each product inside the off plan page
    When Click on Main page "Off-plan"
    Then Verify the right page opens Off-plan
    And Verify each product on this page contains a title and picture visible

  Scenario Outline: User can filter by sale status
    When Click on Main page "Off-plan"
    Then Verify the right page opens Off-plan
    When Set filter by sale status of <filter>
    Then Verify each product contains the <filter>
    Examples:
      | filter         |
      | Announced      |
      | Presale(EOI)   |
      | Start of sales |
      | On sale        |
      | Out of stock   |

  Scenario: User can open product detail and see at least one of the three options are available
    When Click on Main page "Off-plan"
    And Click on the first product
    Then Verify the one of the three options of visualization are architecture, interior, lobby
    And Verify the visualizatoin option are clickable