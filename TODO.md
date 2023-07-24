## DB Constraints

### Library

The name must be unique

### Test Case -> KeywordCall

- The index of a new keyword call has to be the index of the last call plus one


## Validation

### Test Case

- The test sequence cannot be empty


### Test Plan

- Verify that all the libraries referenced in the test cases are imported

- At least one test case must reference the test plan


## UI/UX

- Use jQuery 3.7 to autofocus the autocomplete field
  https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#jquery


### Keyword call

- Show the keyword documentation in a modal


## Test execution

/robotexec
  /static
    /user.id
      /testplan.id-testplan.name
        testplan.name.robot
        keywords.resource
        /timestamp
          output.xml
          log.html


- For test executions older than N months generate the log file from output.xml using rebot


## Performance optimizations

- N + 1 queries
