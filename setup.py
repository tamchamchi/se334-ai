from setuptools import setup, find_packages
import os

# Read the contents of README file if it exists
this_directory = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(this_directory, "README.md")
long_description = ""
if os.path.exists(readme_path):
    with open(readme_path, encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="se334-sentiment-analysis",
    version="1.0.0",
    description="Advanced Multilingual Sentiment Analysis API with FastAPI and Transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nguyễn Duy Tâm Anh",
    author_email="anhndt.work@gmail.com",
    url="https://github.com/anhndt/se334-ai",
    project_urls={
        "Bug Reports": "https://github.com/anhndt/se334-ai/issues",
        "Source": "https://github.com/anhndt/se334-ai",
    },
    packages=find_packages(include=["src", "src.*", "api", "api.*"]),
    package_data={
        "": ["*.yaml", "*.yml", "*.json", "*.txt"],
    },
    include_package_data=True,
    install_requires=[
        # Web Framework
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0",

        # Machine Learning & NLP
        "transformers>=4.35.0",
        "torch>=2.0.0",
        "torchvision>=0.15.0",
        "scikit-learn>=1.3.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",

        # Data Validation & Serialization
        "pydantic>=2.0.0",
        "pydantic-settings>=2.0.0",

        # Configuration & Utilities
        "pyyaml>=6.0",
        "python-dotenv>=1.0.0",
        "tqdm>=4.65.0",

        # Text Processing
        "nltk>=3.8.0",
        "spacy>=3.7.0",

        # Data handling
        "openpyxl>=3.1.0",
        "xlrd>=2.0.0",

        # HTTP & API utilities
        "httpx>=0.25.0",
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
            "mypy>=1.5.0",
        ],
        "docs": [
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.3.0",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "notebook>=7.0.0",
            "ipykernel>=6.25.0",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords="sentiment-analysis, nlp, machine-learning, fastapi, transformers, multilingual",
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "sentiment-api=api.main:main",
        ],
    },
    zip_safe=False,
)
