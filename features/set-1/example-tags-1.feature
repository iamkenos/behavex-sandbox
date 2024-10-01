@one @product-1
Feature: Example Table Tags

  Background:
    Given I have something

  Scenario Outline: Foo From Example 1
    Then I expect something
    @another @this
    Examples:
      | data |
      | 1    |
      | 2    |
    @another 
    Examples:
      | data |
      | 3    |
      | 4    |

  Scenario Outline: Bar From Example 1
    Given I have something
    When I do something
    Then I expect something
    @this
    Examples:
      | data |
      | 1    |
      | 2    |

    Examples:
      | data |
      | 3    |
      | 4    |