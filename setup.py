import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='nums_from_string',  
    version='0.1.1',
    author="Shih-hong Tsai",
    author_email="doublebite@iis.sinica.edu.tw",
    description="Extract numbers from a string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doubleBite/Numbers-from-String",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
 )