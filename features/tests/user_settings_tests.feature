# Created by costa at 5/31/24
Feature: Tests for user settings page
  All testing scenarios for user settings page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

  @smoke
  Scenario: User can access Whatsapp and Telegram communities
    When Click on "Settings" option at the left side menu
    Given Store original window
    When Click on "Support" option
    When Switch to the new window
    Then Verify that URL of window contains api.whatsapp.com
    When Close current page
    And Go back to original window
    And Click on "News" option
    Then Verify that URL of window contains t.me

  Scenario: User can add a project through the settings
    When Click on "Settings" option at the left side menu
    And Click on "Add a project"
    Then Verify that URL of window contains add-a-project
    When Add some test information to the input fields
    Then Verify the right information is present in the input fields
    And Verify “Send an application” button is available and clickable

  Scenario: User can open the community page
    When Click on "Settings" option at the left side menu
    When Click on "Community" option
    Then Verify that URL of window contains community
    And Verify “Contact support” button is available and clickable

  Scenario: User can open the Contact us page
    When Click on "Settings" option at the left side menu
    And Click on "Contact us" option
    Then Verify that URL of window contains contact-us
    And Verify there are at least 4 social media icons
    And Verify “Connect the company” button is available and clickable


  Scenario: User can go to settings and see the right number of UI elements
    When Click on "Settings" option at the left side menu
    Then Verify that URL of window contains settings
    And Verify there are 13 options for settings
    And Verify "connect the company" button is available

  Scenario: User can click on verifications settings option and verify the right page opens
    When Click on "Settings" option at the left side menu
    When Click on the verification option
    Then Verify the right page Verification opens
#    And Verify “upload image” and “Next step” buttons are available



  @mobile_web
  Scenario: MOB_WEB User can access Whatsapp and Telegram communities
    When Click on "Menu"
    Given Store original window
    When Click on "Support" option
    When Switch to the new window
    Then Verify that URL of window contains api.whatsapp.com
    When Close current page
    When Go back to original window
    When Click on "News" option
    Then Verify that URL of window contains t.me

