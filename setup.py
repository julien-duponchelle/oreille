#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

requirements = ["openai", "pydub"]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Julien Duponchelle",
    author_email="julien@duponchelle.info",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="Oreille is a wrapper on OpenAPI Whisper API. It's provide support for long audio files.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description="OpenAPI Whisper support only files that are less than 25 MB. Oreille will break the audio file into chunks of 25 MB's or less.\n\nhttps://platform.openai.com/docs/guides/speech-to-text/longer-inputs\nOreille will also compute the correct timing of the subtitle when merging the output of Whisper. So once you export the subtitle the timestamp of the subtitle will be right.\nYou can open and save WAV files with pure python. For opening and saving non-wav files – like mp3 – you'll need ffmpeg or libav.",
    include_package_data=True,
    keywords="oreille",
    name="oreille",
    packages=find_packages(include=["oreille", "oreille.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/julien-duponchelle/oreille",
    version="0.2.0",
    zip_safe=False,
)
