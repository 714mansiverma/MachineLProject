from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirement(file_path:str)->List[str]:
    '''
    this function will return the list of requirements.
    '''
    require=[]
    with open(file_path,'r') as file_obj:
        require=file_obj.readlines()
        require=[req.replace("\n","") for req in require]
        if HYPEN_E_DOT in require:
            require.remove(HYPEN_E_DOT)
    return require

setup(
    name='mlproject',
    version='0.0.1',
    author='Mansi Verma',
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt')
    
)