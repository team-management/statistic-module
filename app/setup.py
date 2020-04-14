from setuptools import setup, find_packages

setup(name='app',
      version='0.1',
      description='Flask APP for CORE',
      url='',
      author='Alberto Niironen',
      author_email='',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=['flask', 'bson', 'pymongo', 'flask_restful', 'flask_swagger_ui', 'flask_mongoengine',
                        'flask_cors'])
