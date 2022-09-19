from setuptools import setup, find_packages

# Metadata goes in pyproject.toml.
# These are here for GitHub's dependency graph.
setup(
    name='nats-py',
    version='2.2.0',
    description='Nats using nkeys binary built from nkeys go project',
    packages=find_packages(),
    package_data={'': ['bin/win64/nk.exe','bin/linux64/nk','bin/mac64/nk']},
    include_package_data=True,
    install_requires=[],
)