from setuptools import setup, find_packages

setup(
    name="catppuccin_palette",

    version="0.0.2",

    author="Benny Chin",
    author_email="wcchin.88@gmail.com",

    packages=['catppuccin_palette'],

    url="none",

    license="LICENSE",
    description="Quick access for catppuccin colors as a seaborn palette.",

    long_description=open("README.md").read(),

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Visualization',

         'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.7',
    ],

    keywords='catppuccin, catppuccin-matplotlib, seaborn, matplotlib',

    install_requires=[
        "catppuccin-matplotlib", 
        "seaborn"
    ],
)
