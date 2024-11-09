from setuptools import setup, find_packages

setup(
    name = "koduppg_CGI",
    version = "1.0",
    author = "Camilla Rimér Högberg",
    description = "A web-app for counting word frequencies using FastAPI",
    packages = find_packages(),  # Automatically finds all packages in this project
    install_requires = [
        "fastapi",
        "uvicorn"
    ],
)