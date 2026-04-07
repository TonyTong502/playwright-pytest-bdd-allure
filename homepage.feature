Feature: Home Page

  Scenario: Visit homepage
    Given pre-proccessed file name: <file_name> and file content: <file_content>
    When the user goes to Playwright homepage
    Then the user should expect the title to contain Playwright
    And file name should be not empty

    Examples:
      | file_name                  | file_content              | 
      | TEST_A_{YYYYMMDD_HHMM}.txt | content a {YYYYMMDD_HHMM} |
      | TEST_B_{YYYYMMDD_HHMM}.txt | content b {YYYYMMDD_HHMM} |