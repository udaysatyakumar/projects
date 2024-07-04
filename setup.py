from setuptools import find_packages,setup
from typing import List
#create constant
HYPER_E_DOT = "-e ."
#creating function to read the name of packages from requirements.py one by one
def get_requirements(file_path:str)->List[str]:
    """
    THis function will return list of requirements
    """
    #create an empty list
    requirements = []
    #open the file_path i.e; requirements.txt and create object for that file path
    with open(file_path) as file_obj:
        #read the lines one by one from specified path
        requirements = file_obj.readlines()
        #when we read lines \n will add at end so replace it with blank
        requirements = [req.replace("\n","") for req in requirements]
        #remove "-e ." from reqirements.txt
        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)        
    return requirements

#giving all information of the project in setup
setup(
    name='mlproject',
    version='0.0.1',
    author= 'uday',
    author_email='udaysatyakumar42@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
       