from setuptools import setup , find_packages


setup(
    name='pyrestapi',
    version='0.1.0',
    packages=find_packages(include=['pyrestapi', 'pyrestapi.*']),
    install_requires=[
        'Werkzeug==0.15.5'
    ],
    author='Palash Sureka',
    author_email='devpalash1910@gmail.com',
    packages=[
        'pyrestapi','pyrestapi.models','pyrestapi.datastore'
    ]

)