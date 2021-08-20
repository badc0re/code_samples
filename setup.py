from typing import List
from setuptools import setup, find_packages


def _required() -> List[str]:
    with open('requirements.txt') as f:
        required = f.read().splitlines()
    return required


setup(
    name='klarna-solver-service',
    version='0.1',
    description='Klarna solution provider.',
    author='Dame',
    author_email='',
    license='Dame Jovanoski',
    url='',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    install_requires=_required(),
)
