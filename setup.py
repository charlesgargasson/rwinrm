from setuptools import setup, find_packages

setup(
    name='rwinrm',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'pypsrp',
    ],
    entry_points={
        'console_scripts': [
            'rwinrm=src.main:main',
            'rawwinrm=src.main:main',
            'rw=src.main:main',
        ],
    },
)
