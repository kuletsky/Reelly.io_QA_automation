# Created by kuletsky at 12/9/24
Feature: Tests for Product details page
  All testing scenarios for Product details page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

  Scenario: User can open product detail and see at least one of the three options are available
    When Click on Main page "Off-plan"
    And Click on the first product
    Then Verify the one of the three options of visualization are architecture, interior, lobby
    And Verify the visualizatoin option are clickable