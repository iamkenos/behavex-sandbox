@two @product-1
Feature: Example Table Tags 2

  Background:
    Given I have something

  Scenario Outline: Foo From Example 2
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

  Scenario Outline: Bar From Example 2
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