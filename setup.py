from setuptools import setup, find_namespace_packages


APP_NAME = "mlflow_vizmod"
VERSION = "1.1.3"
LICENSE = "MIT"
AUTHOR = "James Hibbard, Andrew Bauman"
DESCRIPTION = "MLflow model flavor for managing visualizations as models"

setup(
    name=APP_NAME,
    version=VERSION,
    license=LICENSE,
    author=AUTHOR,
    description=DESCRIPTION,
    install_requires=[
        "mlflow>=1.11.0",
        "PyYAML>=5.3.1",
        "altair>=4.1.0",
        "altair_viewer>=0.3.0",
    ],
    extras_require={},
    packages=find_namespace_packages("src"),
    package_dir={"": "src"},
    package_data={
        "": ["*.yaml"],
    },
    entry_points="""
    [console_scripts]
    """,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)
