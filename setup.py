from setuptools import find_packages,setup
from typing import List

REQUIREMENTS_FILE_PATH = "requirements.txt"

HYPHEN_E_DOT = "-e ."

requirement_list = []

def get_requirements(FILE_PATH:str)->List[str]:
    with open(REQUIREMENTS_FILE_PATH) as file_obj:
        requirement_list.append(file_obj.readline().replace("\n",""))
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.replace(HYPHEN_E_DOT,"")
    print("*************")
    return requirement_list

    
setup(name="ML Project",
      version="0.0.1",
      author="Saptarshi Sanyal",
      author_email="saparshi.edp@gmail.com",
      packages=find_packages(),
      install_requires=get_requirements(REQUIREMENTS_FILE_PATH)
      )