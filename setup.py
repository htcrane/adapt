from setuptools import setup, find_packages
from pathlib import Path
import platform
import pkg_resources


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

INSTALL_REQUIRES = ["numpy>=1.16", "scipy>=1.0", "scikit-learn>=0.2", "cvxopt>=1.3.0"]

def get_install_requires():
    if platform.system() != 'Darwin':
        INSTALL_REQUIRES.append("tensorflow<2.12")
    else:
        installed_pkgs = [pkg_name.project_name for pkg_name in pkg_resources.working_set]
        if "tensorflow-macos" in ','.join(installed_pkgs):
            INSTALL_REQUIRES.extend(["tensorflow-macos>=2.0","tensorflow-metal"])
        else:
            INSTALL_REQUIRES.append("tensorflow>=2.0")
    return INSTALL_REQUIRES

setup(
    name='adapt',
    version='0.4.3',
    description='Awesome Domain Adaptation Python Toolbox for Tensorflow and Scikit-learn',
    url='https://github.com/adapt-python/adapt.git',
    author='Antoine de Mathelin',
    author_email='antoine.demat@gmail.com',
    license='BSD-2',
    packages=find_packages(exclude=["tests"]),
    install_requires=get_install_requires(),
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown'
)

