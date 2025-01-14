from setuptools import setup, find_packages

exec(open("leetcode_export/_version.py").read())

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="leetcode-export",
    version=__version__,
    url="https://github.com/NeverMendel/leetcode-export",
    license="MIT",
    author="Davide Cazzin",
    author_email="cazzindavide@gmail.com",
    description="Python script to export your LeetCode solutions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["leetcode", "leetcode-solutios", "leetcode-export"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=["dataclasses_json", "requests"],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "leetcode-export=leetcode_export.__main__:main",
        ]
    },
)
