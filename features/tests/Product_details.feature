# Created by rima at 2/28/2022
Feature: Tests for product page


  Scenario: user can select the colors
    When Open Amazon product B07WBXHMT9 page
    Then Verify user can click through colors


  Scenario: user can select the colors
    When Open Amazon product B07BJKRR25 page
    Then Verify user can click through all the colors


  Scenario: User can see the deals, when user hovers over New Arrivals
    Given Open Amazon product B074TBCSC8 page
    When hovers over New Arrivals
    Then verifies user can see the deals of new arrival