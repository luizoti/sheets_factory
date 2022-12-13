"""
    Setup file for sheets_factory.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.3.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
from setuptools import setup

setup(
    name="sheets_factory",
    version="1.0",
    description="Modulo para criar planilhas.",
    author="Luiz Antonio Lazoti",
    author_email="luizlazoti@hotmail.com",
    url="https://github.com/luizoti/sheets_factory.git",
    install_requires=open("requirements.txt", "r").read().split(),
)

if __name__ == "__main__":
    try:
        setup(use_scm_version={"version_scheme": "no-guess-dev"})
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
