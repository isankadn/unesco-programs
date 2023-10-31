from setuptools import setup, find_packages

setup(
    name='unesco_programs',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.2',
        'Pillow',    
        ],
)