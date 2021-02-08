import os

import setuptools

setuptools.setup(
    name='hdy',
    version='2021.02.08',
    keywords='demo',
    description='A demo for python packaging.',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        )
    ).read(),
    author='deryann',
    author_email='deryann@gmail.com',

    url='https://github.com/deryann/hdypackagedemo',
    packages=setuptools.find_packages(),
    license='MIT'
)