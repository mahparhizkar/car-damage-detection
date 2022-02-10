from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Car Damage Detection project is a machie learning project for detection of claim part in image.',
    long_description=readme,
    author='Mahboub Parhizkar',
    author_email='mah.parhizkar88@gmail.com',
    url='https://github.com/mahparhizkar/car-damage-detection',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

