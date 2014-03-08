from distutils.core import setup
from setuptools import find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='django-dropzone-field',
    version='develop',
    packages=find_packages(exclude=["example_project", "example_project.*"]),
    include_package_data=True,
    zip_safe=False,
    url='',
    license='',
    author='Fluxility',
    author_email='contact@fluxility.com',
    description='A Django ImageField using a DropzoneWidget based on dropzone.js',
    long_description=readme()
)
