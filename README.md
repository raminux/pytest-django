# pytest-django
The first question that comes into my mind is that WIFM (What's in it for me?)
## WIFM
1. Getting comfortable using `pytest`. 
2. Testing Django applications
3. Doing various testings
    - Unit tests
    - Integration tests
    - End to end tests
    - Performance tests
    - API tests
    - Black box tests
4. Theoretical testing principles
5. Continuous Integration (CI)
6. Slack notifications
7. Bitbucket pipelines
8. Software development concepts

# What is Pytest?
- the most popular python package for testing
- a feature-rich, plugin-based ecosystem for testing python
- Pytest is not Unittest (another python testing package)
- Provides a new approach for writing tests, namely, functional testing for applications
- Less boilerplate
- Common tasks require less code advanced tasks can be achieved seemingly
- Pytest is explicit!
- Some of the features of Pytest to be discussed in in this repo:
    - Fixtures
    - Custom Markers
    - Parametrize
    - Skip
    - Xfail
    - Pytest-Django
    - Pytest-Xdist
    - Pytest-con

## Some points
- By default, Pytest is looking for files that starts or ends with *'test'*. This behaviour can be configured to find other files. 

## How to install Pytest?
```bash
$> pipenv shell
$> pip install pytest
```

## How to run pytest tests
```bash 
$> pytest . -v
```

