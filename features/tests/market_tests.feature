# Created by kuletsky at 12/11/24
Feature: Tests for Market page
  All testing scenarios for Market page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

  Scenario: User can open market tab and go through the pagination
    When Click on Main page "Market"
    Then Verify the right page Market opens
    And Verify pagination to final page of Market
    And Verify pagination to first page of Market
