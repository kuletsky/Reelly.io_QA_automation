# Created by costa at 5/28/24
Feature: Tests for secondary deals page
  All testing scenarios for secondary deals page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

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


  Scenario: Verify user can open the Secondary deals and go through the pagination
    When Click on "Secondary" option at the left side menu
    Then Verify the right page opens
    When Go to the final page using the pegination button and back


  @mobile_web
  Scenario: MOB_WEB Verify user can filter the Secondary deals by "want to sell" option
    When Click on "Secondary" MOBILE menu
    Then Verify the right page opens
    When Filter the products by Want to sell
    Then Verify that all cards have For sale tag


  @mobile_web
  Scenario: MOB_WEB Verify user can filter the Secondary deals by "want to buy" option
    When Click on "Secondary" MOBILE menu
    Then Verify the right page opens
    When Filter the products by Want to buy
    Then Verify that all cards have Want to buy tag