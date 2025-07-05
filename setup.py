from setuptools import setup, find_packages

setup(
    name='rwinrm',
    version='0.0.5',
    packages=find_packages(),
    install_requires=[
        'gssapi',
        'pypsrp[kerberos] @ git+https://github.com/jborean93/pypsrp',
    ],
    entry_points={
        'console_scripts': [
            'rawwinrm=src.main:main',
        ],
    },
)
