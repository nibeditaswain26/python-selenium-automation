# Created by rima at 3/7/2022
Feature: Tests for 404 page
  #

  Scenario: User is able to navigate to amazon blog from 404 page
    Given Open Amazon product B07WBXHMT9SHKNATUWM page
    And Store original window
    When Click on the dog image
    When Switch to a new window
    Then Verify blog is opened
    And Close blog window
    And Return to original window