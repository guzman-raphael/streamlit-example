from setuptools import setup, find_packages

setup(
    name="utils",
    version="1.0.0",
    install_requires=['datajoint', 'streamlit', 'streamlit_keycloak'],
    packages=find_packages(),
)