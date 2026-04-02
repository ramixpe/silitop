from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name='silitop',
    version='0.1.0',
    author='ramixpe',
    author_email='',
    url='https://github.com/ramixpe/silitop',
    description='Accurate, lightweight terminal monitoring for Apple Silicon',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'silitop = silitop.cli:main',
            'asitop = asitop.asitop:main'
        ]
    },
    project_urls={
        "Source": "https://github.com/ramixpe/silitop",
        "Issues": "https://github.com/ramixpe/silitop/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ],
    keywords='silitop asitop apple-silicon macos monitoring',
    install_requires=[
        "dashing",
        "psutil",
    ],
    zip_safe=False
)
