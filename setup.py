from setuptools import find_packages,setup
from typing import *

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the list of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='khyati',
    author_email='mbi2022006@iiita.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)