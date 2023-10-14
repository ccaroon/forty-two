from setuptools import setup
import forty_two.version

setup(
    name='forty_two',
    url='https://github.com/ccaroon/forty-two',
    maintainer='Craig N. Caroon',
    version=forty_two.version.VERSION,
    packages=[
        'forty_two',
        'forty_two.commands',
        'forty_two.lib'
    ],
    package_dir={'forty_two': 'forty_two'},
    install_requires=[
        'arrow ~= 1.3.0',
        'click ~= 8.1.7',
    ],
    entry_points={
        'console_scripts': [
            'forty_two=forty_two.main:cli',
        ],
    },
)
