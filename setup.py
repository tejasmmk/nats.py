from setuptools import setup, find_packages

# Metadata goes in pyproject.toml.
# These are here for GitHub's dependency graph.
setup(
    name='nats-py',
    version='1.0.0',
    description='Nats using nkeys binary built from nkeys go project',
    packages=find_packages(exclude=["./examples","./tests"]),
    package_data={'': ['bin/win64/nk.exe']},
    include_package_data=True,
    install_requires=[],
)