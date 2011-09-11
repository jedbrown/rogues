from setuptools import setup, find_packages

setup(name             = 'rogues',
      version          = '0.2.2',
      test_suite       = 'nose.collector',
      packages         = find_packages(),
      install_requires = ['numpy', 'scipy'],
      author           = 'Don MacMillen',
      author_email     = 'don@macmillen.net',
      url              = 'https://github.com/macd/rogues',
      description      = "Python and numpy port of Nicholas Higham's m*lab test matrices",
      license          = 'MIT',
      keywords         = 'numpy scipy matplotlib linalg',
      classifiers=[
                     'Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Topic :: Scientific/Engineering :: Mathematics',
      ],
)
