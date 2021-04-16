Feature: Wex Home Page Title
	Scenario: Title is correct on Wex home page
		Given chrome browser is launched
		When  Wex homepage is loaded
		Then verify the title of the webpage
		And close browsers