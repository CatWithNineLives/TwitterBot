import setuptools
# with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="botexecutable",
    version="0.0.1",
    author="Nivedita Singh",
    author_email="niveditasingh0627@gmail.com",
    description="Python executable for a twitter bot.",
    url="https://github.com/CatWithNineLives/TwitterBot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
