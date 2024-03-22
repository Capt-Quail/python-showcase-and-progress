#The file you want to test must always begin with 'test' followed by an
#underscore.
from name_function import get_formatted_name

#The function you want to test must begin with 'test' followed by an
#underscore. 
def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

#You can even test multiple (up to thousands) of tests!
def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'