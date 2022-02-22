# Created by rima at 2/22/2022
Feature: Tests to verify Customer Service’s page UI elements are present.
  # Enter feature description here

  Scenario: User can see all the UI elements in Customer Service’s page
    Given Open Amazon Help Page
    Then verify there is a header
    Then verify there is 9 different link under the header
    Then verify there is a search field
    # Then verify help topics header
    Then verify there is a list of 12 topics under topics header
    Then verify there are 7 images changes according to the topics ,in bottom right corner