# What is Continuous Integration (CI)? 
CI means whenever I commit my changes, there is a server that is taking my changes and doing stuff with them. All this action are done automatically. Actually, CI tools help developers to test their codes before merging those codes to the main branch. The overall procedure is that, the CI tools, build and test the codes, and if there is any test failure or warning, it sends an email to someone who is in charge.  

# How to configure the CI system in Github?
This is a simple, but important note to keep in mind. A CI pipeline runs whenever our code change to make sure all of our changes work with the rest of the code when it’s integrated. It should also compile our code, run tests, and check that it’s functional. A CD pipeline goes one step further and deploys the built code into production.

It is so easy to setup the CI procedure. Just do as it is stated in the following link: [Github CI settings](https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/)

Some points to keep in mind:
1. We need to specify the Python version explicitly.
2. We have to say the pytest where to search for tests. 
3. After each commit, the CI will start to run and test integrity of our code base. 

# 