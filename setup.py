from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='JonUtils',
      version='0.1',
      description='Tools used in preparing data for Chicago analysis project',
      url='https://github.com/hubrigant/chicago_analysis',
      author='Jon',
      author_email='jonhatesspam+jonutils@gmail.com',
      license='Only me, no one else can use',
      packages=['JonUtils'],
      install_requires=[
        'numpy',
        'scipy',
        'shapely',
        'pyproj',
        'geopandas'
      ],
      zip_safe=False)
