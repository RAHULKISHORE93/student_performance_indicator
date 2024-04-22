from setup.tools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path : str)-> List[str]:
    '''This function will return the list of requirements.'''
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'student_performance_indicator', 
    version = '0.0.1',
    author = 'Rahul',
    author_email = 'rahulkishore93@gmail.com'
    
    

)        



    