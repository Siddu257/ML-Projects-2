from setuptools import find_packages, setup
from typing import List

hypen_e_dot = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
    name="MLProject2",  # Name of your project
    version="0.1.0",    # Version of your project
    author="Siddalingesh",  # Your name
    author_email="siddalingesh257@gmail.com",  # Your email
    packages=find_packages(),  # Correctly call find_packages() to return a list of packages
    install_requires=get_requirements("requirements.txt")  # List of dependencies
)
