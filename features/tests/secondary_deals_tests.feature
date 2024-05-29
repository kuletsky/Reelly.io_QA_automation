# Created by costa at 5/28/24
Feature: Tests for secondary deals page
  All testing scenarios for secondary deals page

  Scenario: Verify user can filter the Secondary deals by "want to sell" option
    Given Open the main page
    When Log in to the page
    When Click on "Secondary" option at the left side menu
    Then Verify the right page opens
    When Filter the products by "want to sell"
    Then Verify all cards have "for sale" tag