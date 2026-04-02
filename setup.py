from setuptools import setup, find_packages

long_description = 'Performance monitoring CLI tool for Apple Silicon'

setup(
    name='silitop',
    version='0.1.0',
    author='Timothy Liu',
    author_email='tlkh.xms@gmail.com',
    url='https://github.com/ramixpe/silitop',
    description='Lightweight performance monitoring CLI tool for Apple Silicon',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
        entry_points={
            'console_scripts': [
                'silitop = silitop.cli:main',
                'asitop = asitop.asitop:main'
            ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    keywords='silitop asitop apple-silicon macos monitoring',
    install_requires=[
        "dashing",
        "psutil",
    ],
    zip_safe=False
)
