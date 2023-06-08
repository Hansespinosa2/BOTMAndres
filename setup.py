from setuptools import setup

setup(
    name='BOTMOptimizer',
    version='1.0',
    author='BOTMTeam',
    packages=['BOTMOptimizer'],
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
