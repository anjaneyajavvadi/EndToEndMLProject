from setuptools import find_packages,setup



setup(
    name='MLProject',
    version='0.0.1',
    author='chinnu',
    author_email='anjaneyajavvadi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)