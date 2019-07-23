Feature: Sign up into the system

  Background:
      Given I am looking at the landing page
      And I click on Sign Up button

  @fixture.chrome
  Scenario: I sign up using email and password successfully
    Given that the signup modal is visible
     When I type in valid email and password
      And I click Sign Up button
     Then I should see a terms & conditions modal
     When I agree with terms & conditions
     Then I should see the Congratulations modal

  @fixture.chrome
  Scenario: I sign up using Google account successfully
    Given that the signup modal is visible
     When I click the Sign Up with Google button
     Then I should see a Google Login window open up
     Then I switch to that window
     When I type in my Google email address
      And I click Next to switch to password prompt page
     Then I should see the password input page coming up
     When I type in my Google password
      And I click Next to confirm my authentication
     Then The popup window should be closed
      And I should see a terms & conditions modal
     When I agree with terms & conditions
     Then I should see the Congratulations modal