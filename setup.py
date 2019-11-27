from setuptools import setup, find_packages
from setuptools.command.install_scripts import install_scripts
import shutil


class InstallScripts(install_scripts):

    def run(self):
        install_scripts.run(self)

        for script in self.get_outputs():
            dest = script[:-3]


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
    packages=find_packages(where='.', exclude=(), include=('*',)),
    scripts=["lifep"]
)