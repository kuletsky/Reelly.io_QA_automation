# Created by costa at 5/28/24
Feature: Tests for secondary deals page
  All testing scenarios for secondary deals page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page kuletsky@gmail.com, bJyxsHf5Y@6dnEV

  @smoke
  Scenario: Verify user can filter the Secondary deals by "want to sell" option
    When Click on "Secondary" option at the left side menu
    Then Verify the right page opens
    When Filter the products by Want to sell
    Then Verify that all cards have For sale tag

  @smoke
  Scenario: Verify user can filter the Secondary deals by "want to buy" option
    When Click on "Secondary" option at the left side menu
    Then Verify the right page opens
    When Filter the products by Want to buy
    Then Verify that all cards have Want to buy tag
