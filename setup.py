from setuptools import setup

setup(
    name='BOTMwv',
    version='1.0',
    author='BallingOut',
    packages=['BOTMwv'],
    install_requires=[
        'folium',
        'openrouteservice',
        'numpy',
        'pandas',
        'geopy',
        'gspread',
        'oauth2client',
    ],
)