from setuptools import find_packages, setup

with open("requirements.txt") as f:
    reqs = [line.strip() for line in f]

setup(
    name="docker",
    version="1.0",
    python_requires=">=3.7",
    packages=find_packages(),
    install_requires=reqs,
    entry_points={
    'console_scripts': ['run_main=main:main'],
}
)