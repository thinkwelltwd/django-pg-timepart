import os

from setuptools import setup


def rel(*xs):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *xs)


with open(rel("README.rst")) as f:
    long_description = f.read()


with open(rel("pg_timepart", "__init__.py"), "r") as f:
    version_marker = "__version__ = "
    for line in f:
        if line.startswith(version_marker):
            _, version = line.split(version_marker)
            version = version.strip().strip('"')
            break
    else:
        raise RuntimeError("Version marker not found.")


dependencies = [
    "python-dateutil~=2.7",
]

extra_dependencies = {
    "django": [
        "Django>=2.0,<2.2"
    ],
}

extra_dependencies["all"] = list(set(sum(extra_dependencies.values(), [])))
extra_dependencies["dev"] = extra_dependencies["all"] + [
    # Pinned due to https://bitbucket.org/ned/coveragepy/issues/578/incomplete-file-path-in-xml-report
    "coverage>=4.0,<4.4",

    # Docs
    "alabaster==0.7.12",
    "sphinx==1.8.3",
    "sphinxcontrib-napoleon==0.7",

    # Linting
    "flake8~=3.6.0",
    "isort~=4.3.4",
    "black~=18.9b0",
    "flake8-bugbear~=18.8.0",
    "flake8-quotes~=1.0.0",

    # Misc
    "dj-database-url==0.5.0",
    "psycopg2-binary==2.7.6.1",
    "twine==1.12.1",

    # Testing
    "tox==3.6.1",
    "tox-venv"
]


setup(
    name="django-pg-timepart",
    version=version,
    author="Boyce Li",
    author_email="monobiao@gmail.com",
    description="A Django extension that implements PostgreSQL tables for partitioning and management based on dates.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/chaitin/django-pg-timepart",
    packages=["pg_timepart", "pg_timepart.migrations", "pg_timepart.patch"],
    include_package_data=True,
    install_requires=dependencies,
    extras_require=extra_dependencies,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
