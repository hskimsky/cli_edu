# setup.py

from setuptools import setup, find_packages

setup(
    name="aipcli",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer[all]",
        "boto3",
    ],
    entry_points={
        "console_scripts": [
            "aipcli=aipcli.main:app",
        ],
    },
    author="kyeongseo.oh",
    author_email="kyeongseo.oh@data-dynamics.io",
    description="AWS CLI using Typer",
    python_requires='>=3.6',
)
