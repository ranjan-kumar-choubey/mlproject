from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []  
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        file_obj.close()
        # to remove '\n' with blank
        requirements = [req.replace("\n","")  for req in requirements]

        # this is for removing '-e .' form the requirement
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Ranjan Kumar Choubey',
    author_email='ranjankumarchoubey@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn'],
    install_requires = get_requirements('requirement.txt')
)   