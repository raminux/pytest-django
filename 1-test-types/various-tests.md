# Various Types of Tests

1. Unit test
We want to examine the unit output to a specified input. This is a test that validates functionality of each unit in isolation. 
- Test units in isolation
- Verify code logic
- Fixed input produces a known fixed output
- Easy to write
- Any external dependency should be mocked
- Can simulate errors

2. Integration test
This type of test deals with testing different units and components together. In other words, the contracts between components will be tested to see if everything is hooked up properly. 
- Test multiple components
- Testing contracts
- Testing narrow inputs
- Harder to write
- Don't expose where the problem is
- Tend to be flaky
3. End to end (E2E) test
How our entire system will work from the perspective of a customer. It is a fancy word for a complete integration test. It is obvious that it is much harder to write this type of test. 


==Try to write clean codes not spagetti codes!==