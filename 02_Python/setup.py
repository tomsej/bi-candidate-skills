from setuptools import setup, find_packages

setup(
    name="api_holidays",
    version="1.0",
    packages=find_packages(),
    entry_points={
      'console_scripts': [
          'api-holidays = api_holidays.api_holidays:main',
      ],
    },
)
