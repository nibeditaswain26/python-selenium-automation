# Created by rima at 3/1/2022
Feature: Tests for Amazon Wholefoods page.


  Scenario: Every product on the Wholefoods page has a text ‘Regular’ and a product name.
    When Open Amazon Wholefoods page
    Then Verify that every product on the Wholefoods page has a text ‘Regular’and  its product name.

