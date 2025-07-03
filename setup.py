from setuptools import setup, find_packages

setup(
    name="cieloApi3",
    version="0.2.0",
    author="Rafael Dias",
    author_email="rafaelsd70@gmail.com",
    description="SDK não oficial para integração com a API 3.0 de pagamento da Cielo em Python.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RafaelDias108/API-3.0-Python",
    packages=find_packages(),
    install_requires=['requests', 'future'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.7',
)
