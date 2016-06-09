import os
from setuptools import setup

from django_inline_help import VERSION

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-inline-help',
    version=VERSION,
    packages=[
        'django_inline_help',
        'django_inline_help.templatetags',
        'django_inline_help.migrations',
    ],
    package_data={'django_inline_help': [
        'django_inline_help/templates/django_inline_help/*',
        'django_inline_help/static/django_inline_help/*'
    ]},
    include_package_data=True,
    license='MIT',
    description='An app for creating changeable tips.',
    author='Bakuutin',
    author_email='igorbakutin@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django >=1.7',
    ]
)
