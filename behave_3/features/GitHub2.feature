#Author: Michelle Scheuer



Feature: Github showing incorrect password with invalid password parameter
	
	Scenario: Failed login attempt to Github
		Given Chrome browser is launched
    When Github is loaded
    And I click on Sign in
    Then I am taken to the login page
    And I enter username "mscheuer92" and password "fakepwd"
    And Click the login button
    Then I am shown a message saying "Incorrect username or password"
    
  Scenario Outline: Login to GitHub with multiple parameters
    Given Chrome browser is launched
    When Github is loaded
    And I click on Sign in
    Then I am taken to the login page
   	And I enter username "<username>" and password "<password>"
  	And Click the login button
   	Then I am shown a message saying "Incorrect username or password"
   
    Examples:
   		| username   | password   |
   		| mscheuer   | fakep      |
   		| mscheuer92 | mscheuer92 |
   		| lisa			 | smith		  |
   		
   		
   	