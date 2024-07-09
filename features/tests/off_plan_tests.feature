# Created by costa at 7/8/24
Feature: Tests for Off-plan page
  All testing scenarios for Off-plan page are located here

  Background:
    Given Open the main page
    When Click on the "Open in browser"
    When Log in to the page kuletsky@gmail.com, bJyxsHf5Y@6dnEV

  Scenario: Verify that all projects are shown
    When Click on Main page "Off-plan"
    Then Verify that all projects are shown

