from setuptools import find_packages, setup

setup(
    name="asciifier",
    packages=find_packages(include=["asciifier"]),
    version="0.1.0",
    description="Converts an Image file into ASCII Art",
    author="fforrespect",
    install_requires=["Pillow==10.1.0", "numpy==1.26.2", "setuptools==69.0.3"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
