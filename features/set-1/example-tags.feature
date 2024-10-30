Feature: Example Table Tags

  Background:
    Given I have something
@asdf
  Scenario Outline: Foo From Example 1
    Then I expect something

    Examples:
      | data |
      | 1    |
      | 2    |
@asdf
  Scenario Outline: Foo From Example 2
    Then I expect something

    Examples:
      | data |
      | 1    |
      | 2    |
