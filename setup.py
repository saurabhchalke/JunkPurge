from setuptools import setup, find_packages

setup(
    name='junkpurge',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'junkpurge=junkpurge.clean_build_dirs:main',
        ],
    },
    author='Saurabh Chalke',
    author_email='saurabh.chalke@example.com',
    description='A tool to clean up build directories in various programming languages.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/saurabhchalke/JunkPurge',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
