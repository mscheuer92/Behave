#Author: Michelle Scheuer

Feature: ODU Computer Science Web Page

  Scenario: Verify ODU has Computer Science Program Page
    Given Chrome browser is launched
    When ODU homepage is loaded
    And Find Program is clicked
    Then I validate that Computer Science & Math hyperlink is present
    And I click on the hyper link 
    Then I search for Computer Science
    And click on the hyperlink
    Then I will be on the Computer Science Program Page
