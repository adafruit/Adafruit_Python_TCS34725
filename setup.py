try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'Adafruit_TCS34725',
      version           = '1.0.3',
      author            = 'Tony DiCola',
      author_email      = 'tdicola@adafruit.com',
      description       = 'Python code to use the TCS34725 color sensor with the Raspberry Pi & BeagleBone Black.',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/adafruit/Adafruit_Python_TCS34725/',
      dependency_links  = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5'],
      install_requires  = ['Adafruit-GPIO>=0.6.5'],
      packages          = find_packages(),

      long_description = long_description,
      long_description_content_type = 'text/markdown')
