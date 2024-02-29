from setuptools import setup, find_packages

setup(
    name='httpAlive',
    version='1.0.2',
    description='HttpAlive is a web probing tool designed for discovering alive subdomains and URLs.',
    author='Bande Aashish',
    url='https://github.com/aashishsec/httpAlive',
    packages=find_packages(),
    install_requires=[
        'requests',
        'httpx',
        'colorama',
    ],
    extras_require={
        'dev': ['argparse'],
    },
    entry_points={
        'console_scripts': [
            'httpAlive = httpAlive.httpAlive:main',
        ],
    },
)
