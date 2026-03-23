from setuptools import find_packages,setup ##find_package will think every __init__ file as a package and it will search for that package
from typing import List

def get_requirements()->List[str]:
    """This funnction will return list of requirments"""
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ##Read lines from the file
            lines=file.readlines()
            ##Process each line
            for line in lines:
                requirement=line.strip()
                ##ignore the empty lines and -e . 
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst
setup(
    name="NetworkSeccurity",
    version="0.0.1",
    author="Datta Kaleswar",
    author_email="dattakaleswar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
