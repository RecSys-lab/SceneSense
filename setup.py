from setuptools import setup, find_packages

setup(
    name="MoVieFex",
    version="1.0.0",
    maintainer='Ali Tourani',
    author="Ali Tourani, Yashar Deldjoo",
    author_email="a.tourani1991@gmail.com",
    description="A multimodal video movie recommendation system",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RecSys-lab/MoVieFext",
    packages=find_packages(include=["moviefex", "moviefex.*"], exclude=['docs', 'examples', 'rtd']),
    include_package_data=True,
    python_requires=">=3.10",
    entry_points={
        'console_scripts': ['blenderproc=blenderproc.command_line:cli'],
    },
    install_requires=[
        "pandas>=2.0",
        "numpy>=1.26",
        "opencv-python>=4.9",
        "matplotlib>=3.9",
        "pytube>=15.0",
        "scipy>=1.14.1",
        "requests>=2.32",
        "PyYAML>=6.0.1",
        "tensorflow>=2.17.0"
    ]
)
