import pytest

# description of pytest concept inside the code 
''' Why ptest?
It is the most popular python package for testing. There are other options such as 
unittest and nose. But, of course, Pytest is the best! 
It provides a plugin-based ecosystem for testing python applications. Some of the
most popular plugins include pytest-django, pytest-cov, pytest-xdist. It provides a 
functional testing approach for applications. It is extremely easy to write 
tests with Pytest. Pytest is so explicit, and as a result, it is easy to write and read tests.
Some of the most important features of Pytest are:
- Fictures, Custom markers, Parametrize, Skip, Xfail, Pytest-Django, Pytest-Xdist, Pytest-cov. 

'''


'''
Contents:
- Test functions
- Markers
- Skip, Skipif
- Fixtures
- Parametrize
'''

# Pytest finds test files by adding test_ to our test file name. This behavior is configurable!
# Also, test functions must be started with test_ prefix!

'''  
To run tests, just use the following command
$ pytest .
Or with more verbosity:
$ pytest test_gist.py -v
'''
''' 
The following test function returns None, and also will fail because 1 is not equal to 2.
'''
def test_our_first_test() -> None:
    assert 1 == 2


# The following marker will tell the pytest to skip the test, so it will not be run by test!
@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2

# To skip a test with a certain condition use skipif marker with suitable condition
@pytest.mark.skipif(4 > 1, reason='Skipped because 4 in greater than 1')
def test_should_be_skipped_if() -> None:
    assert 1 == 0

'''
To tell the pytest to continue testing even if a function failed, use xfail marker.
The following test function will fail, but it is counted as xfailed ones. 
If we change assert 3 == 3, then the test will xpassed!
'''
@pytest.mark.xfail
def test_doesnot_care_if_fails() -> None:
    assert 3 == 0


# We can also add our own markers. For example, if a test is slow, we can mark it as slow test!
# To define a new marker, we need to edit a file called pytest.ini file. 

''' Pytest command-line useful examples:
1- To skip warnings:
$ pytest test_gist.py -v -p no:warnings
2- To run a specific markers (for example slow marked tests)
$ pytest test_gist.py -v -m slow
$ pytest test_gist.py -v -m "not slow"
'''

@pytest.mark.slow
def test_with_custom_mark() -> None:
    pass


''' Pytest Fixture
It is a method to setup some data or feature into the experiment, for example initializing a database. 
Consider the following class
'''

class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol
    
    def __str__(self):
        return f'{self.name}:{self.stock_symbol}'

# The following fixture is a company that creates a Company object.    
@pytest.fixture
def company() -> Company:
    return Company(name='Fiver', stock_symbol='FVRR')

def test_with_fixture(company: Company) -> None:
    print(f'Printing {company} from fixture.')

'''
To see the print outputs during the test, just add -s argument to the pytest commandline:
$ pytest test_gist.py -v -s
'''

''' Pytest Parametrize
It is the Pytest's elegent way to test some functionality for various inputs or data.
'''

@pytest.mark.parametrize(
    "company_name", 
    ['TikTok', 'Instagram', 'Twitch'],
    ids=['TIKTOK TEST', 'INSTAGRAM TEST', 'TWITCH TEST']
)
def test_parameterize(company_name: str) -> None:
    print(f'\n Test with {company_name}')
