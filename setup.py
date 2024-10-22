'''
The setup.py file is an essential part of packaging and 
distributing Python Projects. It is used by setuptool
(or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more
'''

#find_packages -  scan through all the folders and wherever there is an __init__.py file it will consider that folder as an package
#setup -  responsible to provide all the information about the project
from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:
    """
    this function will return list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # read lines from the file
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('No requirements.txt file found')

    return requirement_lst

print(get_requirements())