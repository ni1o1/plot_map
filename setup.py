import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="plot_map",
    version="0.1.8",
    author="Qing Yu",
    author_email="qingyu0815@foxmail.com",
    description="A tool to add basemap in matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/ni1o1/plot_map",
    project_urls={
        "Bug Tracker": "https://github.com/ni1o1/plot_map/issues",
    },
    install_requires=[
        "geopandas","matplotlib"
        ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Framework :: Matplotlib",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
