from setuptools import setup

setup(name='my_hello_tozzo',
    version='0.1',
    author='Paulo',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    description=('testtesttesttesttesttesttesttest'),
    scripts=['scripts/hello.py'],
    install_requires=[
          'numpy>=1.0'
      ],
    packages=['my_hello']
    )
