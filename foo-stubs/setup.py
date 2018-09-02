from distutils.core import setup

setup(
    name="foo-stubs",
    version="0.1",
    package_data={"foo-stubs": ['__init__.pyi']},
    packages=["foo-stubs"]
)
