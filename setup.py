from setuptools import setup, find_packages

setup(
    name="evomem",
    version="0.1.0",
    description="Evolutionary Memory System for capturing AI-human interactions and advancing Green AI.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Andrés Salazar Quintero",
    author_email="asalazar@inecore.com",
    url="https://github.com/razalazar/AMK",
    packages=find_packages(exclude=["tests*", "examples*", "docs*"]),
    install_requires=[
        # Core is independent, no strict requirements for basic usage
        # "pydantic>=2.0", # Optional but good for structured data if added later
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
)
