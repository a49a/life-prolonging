from setuptools import setup, find_packages

setup(
    name="life-prolonging",
    version="0.0.2",
    keywords=["tool", "health"],
    license="MIT Licence",
    url="https://github.com/deadwind4/life-prolonging",
    author="deadwind",
    author_email="deadwind4@outlook.com",
    description="代码帮你选择",
    long_description="",
    install_requires=[
        'toml',
    ],
    packages=find_packages(where='.', exclude=(), include=('*',)),
    entry_points={
        "console_scripts": [
            'lpl = lpl:cli'
        ]
    },
    scripts=["lpl.py"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),
)