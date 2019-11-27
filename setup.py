from setuptools import setup

setup(
    name="life-prolonging",
    version="0.0.1",
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
    packages=["lplib"],
    scripts=["lifep"]
)