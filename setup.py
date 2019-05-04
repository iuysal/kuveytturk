import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kuveytturk",
    version="1.0.1",
    author="Ibrahim Uysal",
    description="A Python wrapper for the Kuveyt Turk API",
    url="https://github.com/iuysal/kuveytturk",
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=[
        "six>=1.12.0",
        "requests>=2.21.0",
        "pycrypto>=2.6.1",
    ],
    keywords="python kuveytturk api",
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)