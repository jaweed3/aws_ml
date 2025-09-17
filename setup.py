from setuptools import find_packages,setup
from typing import List

HYPEN_DOT = '-e .'

def get_requirements(filepath: str) -> List:
    """
    this function return list of package requirements.
    """
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)

    return requirements

setup(
    name="aws_ml",
    version='0.0.1',
    author='jaweed3',
    author_email='wedjaw22@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
