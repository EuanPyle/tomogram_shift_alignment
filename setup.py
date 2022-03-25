"""
PEP 517 doesn\u2019t support editable installs
so this file is currently here to support "pip install -e ."
"""
from setuptools import setup

setup(
    use_scm_version={"write_to": "tomogram_shift_alignment/version.py"},
    setup_requires=["setuptools_scm"],
)
