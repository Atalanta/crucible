import os
from setuptools import setup, find_packages

version = '0.1.0'

description = "A generator of strong yet memorable passwords"
cur_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README.rst')).read()
except:
    long_description = description

setup(
    name = "crucible",
    version = version,
    url = 'http://github.com/Atalanta/crucible',
    license = 'MIT',
    description = description,
    long_description = long_description,
    author = 'Stephen Nelson-Smith',
    author_email = 'stephen@atalanta-systems.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
    entry_points="""
[console_scripts]
crucible = crucible.crucible:main
""",
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python'
    ]
)

