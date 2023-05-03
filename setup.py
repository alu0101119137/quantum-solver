import setuptools

readme = open("./README.md", "r")

setuptools.setup(
    name = "quantumSolverTool",
    version = "0.0.4",
    author = "Andrea Hernández",
    author_email = "alu0101119137@ull.edu.es",
    description = "A little quantum toolset developed using Qiskit",
    long_description =  readme.read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/alu0101119137/quantum-solver",
    project_urls = {
        "Bug Tracker": "https://github.com/alu0101119137/quantum-solver/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
    install_requires = [
        'numpy>=1.19.5',
        'matplotlib==3.4.2',
        'qiskit==0.34.1',
        'pwinput==1.0.2',
        'halo==0.0.31',
        'alive-progress==2.3.1',
        'ascii_graph==1.5.1',
        'werkzeug>=0.11.15',
        'oauthlib>=3.0.0',
        'pytz>=2017.3',
        'setuptools',
        'flask',
        'flask-cors',
        'APScheduler',
        'pylatexenc'
    ],
    include_package_data=True
)