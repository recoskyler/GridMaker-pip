from setuptools import setup, find_packages

setup(
    name='gridmaker',
    version='1.0',
    license='Apache 2.0',
    author="Adil Atalay Hamamcioglu",
    author_email='recoskyler224@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/recoskyler/GridMaker',
    keywords='grid image processing maker generator url json',
    install_requires=[
        'PIL',
        'fileinput',
        'json',
        'colorama',
        'requests',
        're',
        'os',
        'hashlib',
        'base64',
        'math',
        'argparse',
    ],
    python_requires=">=3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: Image Processing",
    ]
)