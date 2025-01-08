Feature: Tests for verification page
  All testing scenarios for verification page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page

  Scenario: User can click on verifications settings option and verify the right page opens
    When Click on "Settings" option at the left side menu
    When Click on the verification option
    Then Verify the right page Verification opens
    And Verify “upload image” and “Next step” buttons are available
